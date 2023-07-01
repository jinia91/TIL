# Dirty
- 리눅스에서 Dirty란 커널의 메모리영역중 dirty page라 불리는 영역
- 메모리에 현존하는 정보와 외부장치의 정보 싱크가 필요한 영역을 칭하는 의미로, JPA dirty checking 도 여기서 온말인듯?

## Dirty Page란?
- 리눅스에서 파일 I/O가 일어날 때 커널은 pageCache를 이용해서 디스크에 있는 파일의 내용을 메모리에 저장, 필요할때 캐시에 접근해서 사용
- 쓰기,수정작업이 이루어질경우 Dirty 비트 on
- flush를 통해 dirty page를 디스크로 동기화
- 또한 커널 파라미터를 통해 자동 동기화
- 서버의 워크로드에 따라 이 동기화를 튜닝할 필요도 간혹존재

## Drity Page 관련 커널 파라미터
    sysctl -a | grep -i dirty

<img width="579" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/c14e0ef4-26ba-4814-ae6d-43b1053c729e">

- dirty_background_ratio : dirty page가 이 비율보다 커지면 백그라운드에서 동기화시작
- dirty_background_bytes : 절대값으로 기준
- dirty_ratio : dirty_background_ratio와 동일한 기준이나, 넘을시 i/o가 멈추고 해당 스레드가 동기화
- dirty_bytes: 위와 동일
- dirty_writeback_centisecs : flush 커널 스레드를 몇 초 간격으로 깨울 것인지를 결정
- dirty_expire_centisecs : dirty_writeback_centisecs로 일어난 커널 스레드가 어떤 기준으로 동기화할지를 정하는것으로 dirty_expire_centisecs 이상 동기화하지 않은 오래된 dirty page를 동기화한다.

위의 방식은 완전히 독립적이지 않음!

- dirty_ratio 최소값은 5
- dirty_background)ratio가 dirty_ratio보다 크다면 강제로 dirty_ratio가 절반값으로 수정됨
- dirty_background_ratio ,dirty_background_bytes 값이 설정되어 있다면 dirty_ratio, dirty_bytes는 무시
- dirty_ratio 이상으로 dirty page가 생성되는 상황이면 성능저하

## dirty page관련 파라미터가 변경될 경우 I/O 패턴의 변화
### 1. ratio가 높을경우
> isostat 으로 I/O사용량을 보기
대부분 0이다가 갑자기 100%에 이르는 패턴
배치성 동기화이기 때문
### 2. ratio를 낮춰 빠르게 비우게하면?
더 자주 flush 커널 스레드가 깨어나지만, 한번에 동기화시켜야할 양이 적기때문에 I/O 사용량이 5~90%대

### insight?
- 멀티스레드 환경의 애플리케이션의 경우 불필요하게 자주 깨어나는 flush 커널 스레드는 컨텍스트 스위칭을 요하므로 그만큼 오버헤드, cpu 리소스 낭비
- 하지만 주기를 길게 갖고 I/O를 한다하더라도 결국은 받아들이는 다운스트림영역의 쓰로풋(처리율)이 dirt page가 생기는 속도보다 느리다면? 지연이 생길수밖에 없다!
- 결국 캐시이지만 처리율을 고려한 waiting queue의 개념도 있기때문
- 처리양 == dirty page amount 가 제일 바람직
