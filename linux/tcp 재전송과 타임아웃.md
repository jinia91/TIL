# TCP의 특징
- 연결 지향적 (Connection-oriented): TCP는 데이터를 전송하기 전에 송신자와 수신자 사이에 연결을 설정. 이 연결은 데이터 전송이 완료될 때까지 유지된다.

- 데이터의 순서 보장: TCP는 각 데이터 패킷에 순서 번호를 부여하여 전송

- 오류 복구: TCP는 수신 측이 데이터 패킷을 받았다는 확인(ACK)을 송신 측에 보내야한다. 송신 측이 확인 응답을 일정 시간 내에 받지 못하면 해당 데이터 패킷을 다시 보낸다.

- 흐름 제어 (Flow Control): TCP는 수신 측이 처리할 수 있는 만큼만 데이터를 보낸다. 이는 수신 측이 혼잡하지 않은 상태에서 데이터를 받을 수 있도록 보장.

- 혼잡 제어 (Congestion Control): 네트워크 경로 상에 혼잡이 발생할 경우, TCP는 데이터 전송 속도를 줄여서 혼잡을 완화하는 메커니즘을 가지고 있음.

- 데이터 무결성: TCP 헤더에는 체크섬이 포함되어 있어, 데이터가 손상되거나 변경되는 것을 감지할 수 있음.

## SACK, DACK

### Selective Acknowledgment (SACK)
- SACK은 TCP의 오류 복구 메커니즘을 향상시키는 데 사용된다. 
- 기본적으로 TCP는 순차적으로 데이터 패킷을 전송하며, 수신 측은 순서대로 패킷을 받음. 만약 패킷이 유실되면, 수신 측은 유실된 패킷 이후로 받은 모든 패킷에 대한 ACK를 보내지 않으며 모든 대상 패킷을 재전송 받게됨
- 이와 달리 SACK을 사용하면, 수신 측은 유실되지 않은 패킷에 대해 개별적으로 ACK를 보낼 수 있다. 이는 송신 측이 유실된 패킷만 재전송하도록 해서 네트워크 대역폭을 보다 효율적으로 사용하게 한다.
- 추가적인 처리 오버헤드와 복잡성 문제가 존재

### Delayed Acknowledgment (Delayed ACK)
- Delayed ACK는 네트워크의 효율성을 높이는 기술로, 수신 측이 패킷을 즉시 ACK하지 않고 약간 지연시켜서 ACK를 보내는 방법
- Delayed ACK의 주요 목적은 여러 패킷에 대한 ACK를 하나로 묶거나, ACK와 다른 데이터를 함께 보내서 네트워크 대역폭을 보다 효율적으로 사용하는 것
- 하지만 이 지연설정이 RTO보다 길경우 불필요한 재전송이 발생할 수 있으므로 세부적인 튜닝이 필요

## 오류 복구와 재전송, RTO(Retransmisson Timeout)

### RTO
> RTO : ack을 기다리는 시간
- 일반적으로 RTT(RoundTripTime, 두 종단간 패킷전송에 필요한 시간)을 기준으로 자동 세팅된다.
- 하지만 TCP HandShake의 첫 syn처럼 RTT를 알지 못하는 상황에서는 초기 설정치인 InitRto가 세팅된다.

`ss -i`

<img width="270" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/e1ca36dd-8554-4bd9-bd49-3d3463b64129">

- 현재 연결되어있는 세션들의 rto 확인 가능(ms단위)

- 만약 재전송이 일어날경우 RTO는 기존 값의 x2가 된다.

`sysctl -a | gep -i retries`

    net.ipv4.tcp_syn_retries = 6
    net.ipv4.tcp_synack_retries = 5
    net.ipv4.tcp_orphan_retries = 0
    net.ipv4.tcp_retries1 = 3
    net.ipv4.tcp_retries2 = 15
    
    
- `net.ipv4.tcp_syn_retries = 6` : tcp 3way handshake의 첫 syn에 대한 재시도 횟수, 애플리케이션 레이어에서 정하는 connectionTimeout과는 별개로, os 커널레벨에서 tcp 세션 연결시 syn 연결에 대한 최대 요청 횟수가 존재하는 셈
rto는 지수적으로 증가하므로 6이면 최초 1초부터 총 7번 재시도를 보내며 최초 syn을 보내고 63초 후 마지막 syn을 보내게 된다. 보통 connectionTimeout은 짧게 잡으므로(3~5초) 실제론 syn을 3번정도 보내게 되려나?

- `net.ipv4.tcp_synack_retries = 5` : syn 에 대한 응답 syn-ack을 몇번 리트라이할지
- `net.ipv4.tcp_orphan_retries = 0` : 고아소켓이란 FIN_WAIT1 상태의 소켓으로 fin을 받고 아직 그에 대해 ack을 받지 못해 리소스가 회수되지 못한 상태의 소캣을 의미하며 fin의 ack을 받기위해 재시도하는 횟수를 의미한다
여기서 디폴트가 0이여도 내부 커널소스상에서 디폴트를 7~8로 집어넣으므로 실제론 fin을 여러번 재시도하게된다. 
- `net.ipv4.tcp_retries1 = 3`, `net.ipv4.tcp_retries2 = 15` : soft threshold, hard threshold로 간주, 첫번째는 ip 레이어의 상태체크, 두번쨰는 더이상 통신을 할수 없다고 판단하는 기준

## 재전송 추적

### trcretrans 스크립트 사용해보기

## RTO 수정하기
- 기본적으로 RTO는 200(ms)이하로 내릴수 없음 - RTO_MIN = 200
- 최댓값은 120초
- 대략적으로 RTO_MIN + RTT_MAX로 값이 구해짐
- 하지만 만약 aws 기준으로 같은 리전에 있는 ec2와 rds 간에는 rto가 204나 될 이유가 없다. 대충 50ms만 넘어도 이는 유실로 볼 수 있기때문
- 이럴때 변경방법은?

### ip route
`ip route change defult via <gw> dev <device> rto_min 100ms`
![image](https://github.com/jinia91/TIL/assets/85499582/af9aa7e4-44d9-4413-bb8c-2fa5a9635c0a)

ip route를 통해 나오는 default 뒤의 부분을 위의 커맨드에 넣어주면 됨!

=> `ip route change '여기!' rto_min 100ms`

내부통신만 하는 서버 혹은 세션의 경우라면 rto 튜닝은 약간이라도 더 효율적인 통신을 가능하게 할 수 있을것


## application 타임아웃 세팅 팁!

- ConnectionTimeOut 권장값 : 3s - 기본적인 initRto 값이 1s 이므로 최소 1s 이상은 세팅하는것이 바람직 
- ReadTimeOut 권장값 : 300ms 이상 이라곤하는데... 일단 재전송 1~2회를 감안한 값으로 정하는것이 바람직
