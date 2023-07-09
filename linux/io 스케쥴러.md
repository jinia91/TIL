# I/O Scheduler의 필요성
## I/O Scheduler란?
상대적으로 접근 속도가 느린 I/O 장치, 즉 디스크에 대한 성능을 최적화하기 위해 `Block I/O Layer`와 블록 디바이스 사이에 job의 순서를 관리해주는 역할

- 단순 비동기 작업간의 throughPut 제어라면 그냥 queue만 존재하면됨
- 하지만 디스크의 특성상 요청을 섹터 순서대로 정렬했을때 성능 향상이 크므로 이와같은 하드웨어 동작에 대한 최적화가 필요
- 하지만 ssd를 사용하는 최신 환경, 특히 NVMe ssd라면 이미 모든 메모리에 대한 접근이 거의 동일한(메모리 주소 위치에 따라 물리적인 차이가 존재하므로 완전히 동일하지는 않을것) 시간복잡도를 가지며, 병렬 IO도 지원하기때문에 프로세스간 공정 스케쥴러의 동작 자체조차 오버헤드라 스케쥴러가 불필요한 경우가 많다.
- NVMe라면 가장 최신 알고리즘인 BFQ MQ조차 필요없는거같음

## I/O Scheduler의 종류

### CFQ I/O 스케쥴러
> Completely Fair Queueing

- 완전 공정 대기열
- 현재는 deprecated되어 삭제됨(Kernel 5.0부터), Budget Fair Queueing (BFQ)으로 대체되었다고 함

- 기본적인 동작은 우선순위에따라 class를 나누고(RT, BE, IDLE), 동작 형태에 따라 타입을 나눈다음(SYNC, SYNCE_NOIDLE, ASYNC) 각 프로세스별로 큐를 두고 해당 큐는 직전 작업 헤드위치에 따라 정렬을 최적화 하면서 라운드 로빈으로 큐를 순환하여 poll하는 방식

## Deadline I/O 스케쥴러

  I/O 요청별로 Deadline을 정하고 되도록 그 시간안에 완수될 수 있도록 동작하는 방식

  - type을 Read와 Write로 분리하고 각 타입별로 Sorted list와 FiFO list를 둔다. Sorted는 섹터 기준으로 정렬되며 기본 동작은 sorted된 리스트를 큐로 사용하여 동작한다.
  - 만약 fifo에서 deadline을 넘긴 요청이 존재함다면 해당 요청을 꺼내서 처리한다.


## Noop I/O 스케쥴러

- 순수 병합작업만 실행하는 I/O 스케쥴러
- ssd의경우 헤더를 움직일필요가없으므로 무의미한 정렬을 제거


## 비고 

`iostat`

<img width="1081" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/57f5a059-f023-4d15-bc26-207297f64238">

`iotop`

aws ec2에서는 존재하지 않는듯? 

io 스케쥴링 자체가 ssd 시대이후엔 크게 중요하지 않은거같다. 

스케쥴링 전략 자체를 알아두다가 나중에 스케쥴링을 구현할 일이 있을때 참고하는 정도면 충분하지않을까



