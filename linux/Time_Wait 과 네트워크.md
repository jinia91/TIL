# TCP
## TCP 특징
- 연결형(connection-oriented) 서비스로 연결이 성공해야 통신이 가능하다.
- 데이터의 경계를 구분하지 않는다.
- 데이터의 전송 순서를 보장한다. 데이터의 순서유지를 위해 각 바이트마다 번호가 부여됨.
- 신뢰성 있는 데이터를 전송한다.(Sequence Number, Ack Number)
  - Sequence Number : TCP 세그먼트의 연속된 데이터 번호
  - Ack Number : 상대방으로부터 받아야하는 다음 TCP 세그먼트 데이터 번호
- 데이터 흐름 제어(수신자 버퍼 오버플로우 방지) 및 혼잡 제어(패킷 수가 과도하게 증가하는 것 방지)
- 연결의 설정(3-way handshaking), 해제(4-way handshacking)
- 전이중(Full-Duplex), 점대점(Point to Point) 서비스

## 3 way handshake
- 1way : (SYN) 클라이언트가 서버에 SYN 패킷을 전송하여 연결 요청을 시작. 이 패킷은 초기 시퀀스 번호인 ISN(Initial Sequence Number)를 포함하고 있으며, 이 번호는 보통 임의로 선택되고 이후 전송되는 데이터 바이트의 순서를 결정하는 데 사용.

- 2way : (SYN+ACK) 서버가 SYN 패킷을 받으면, 자신의 ISN을 포함한 SYN 패킷과 클라이언트의 SYN을 확인(ACK)하는 패킷을 동시에 전송한다. 여기서 ACK 값은 클라이언트의 ISN+1.

- 3way : (ACK) 마지막으로 클라이언트는 서버의 SYN을 확인(ACK)하는 패킷을 전송. 이때의 ACK 값은 서버의 ISN+1

## 4 way handshake

- 1way(FIN) : 연결을 끊으려는쪽(active)에서 FIN 플래그를 설정한 패킷을 전송하여 연결 종료를 요청. 이 패킷은 "나는 더 이상 보낼 데이터가 없으므로 연결을 닫아도 좋다"라는 의미.

- 2way(ACK) : 상대(pasive)는 FIN 패킷을 수신하면 이를 확인하는 ACK 패킷을 FIN 요청자에게 전송. 이 ACK 패킷은 FIN 패킷을 수신했다는 것을 알리는 신호.
- 
- 3way(FIN) : 이제 상대가 FIN. 이는 "나도 더 이상 보낼 데이터가 없으므로 연결을 닫아도 좋다"는 의미를 가지며, 이 단계를 통해 양방향 통신 모두가 종료되게 됩니다.

- 4way (ACK) : 마지막으로, 최초 FIN 송신자는 FIN 패킷을 확인하는 ACK 패킷을 전송. 이 ACK 패킷이 전송되고 나면 TCP 연결은 완전히 종료되며, 모든 자원은 운영 체제에게 반환.

## TCP state

- LISTEN : 서버의 데몬이 떠서 접속 요청을 기다리는 상태
- SYN-SENT : 로컬의 클라이언트 어플리케이션이 원격 호스트에 연결을 요청한 상태
- SYN_RECEIVED : 서버가 원격 클라이언트로부터 접속 요구를 받아 클라이언트에게 응답을 하였지만 아직 클라이언트에게 확인 메시지는 받지 않은 상태
- ESTABLISHED : 3 way-handshaking 이 완료된 후 서로 연결된 상태
- FIN-WAIT1, CLOSE-WAIT, FIN-WAIT2 : 서버에서 연결을 종료하기 위해 클라이언트에게 종결을 요청하고 회신을 받아 종료하는 과정의 상태
- TIME-WAIT : 연결은 종료되었지만 분실되었을지 모를 느린 세그먼트를 위해 당분간 소켓을 열어두고 있는 상태
- CLOSING : 흔하지 않지만 주로 확인 메시지가 전송도중 분실된 상태
- CLOSED : 완전히 종료

## NGINX로 실제 3way, 4way 확인해보기
1. `docker run -it -p 80:80 centos:7 /bin/bash`
2. docker centos7에서 `yum install epel-release`
3. `yum install nginx`
4. `yum install tcpdump`
5. `nginx`
6. `tcpdump -A -vvv -nn port 80 -w server_dump.pcap`
7. `curl http://localhost:80` 
8. 덤프 파일 docker cp로 가져와서 와이어사크로 보기
9. `tcpdump -A -vvv -nn port 80 -w server_dump.pcap`ㅎ
10. `tcpdump -A -vvv -nn port 80 -w server_dump.pcap

<img width="1453" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/78643bfe-dff6-48f5-a718-47a6b480bed5">

1. 클라이언트가 서버의 80번 포트로 SYN 패킷을 전송하여 연결을 요청한다. 이때 초기 시퀀스 번호는 0(3way-1)

2. 서버가 SYN-ACK 패킷으로 응답. 이때 서버의 초기 시퀀스 번호는 0이고, 클라이언트의 SYN을 확인하였으므로 ACK 번호는 1(3way-2)

3. 클라이언트가 서버의 SYN을 확인하는 ACK 패킷을 전송. 이때 시퀀스 번호는 1(자신이 전송한 SYN 패킷에 대한 응답이므로)이고, ACK 번호는 1(서버의 SYN 패킷을 확인했으므로). 이로써 3-way handshake가 완료되고 TCP 연결이 설정(3way-3)

4. 클라이언트가 HTTP GET 요청을 전송.

5. 서버가 ACK 패킷을 전송하여 클라이언트의 GET 요청을 수신했다는 것을 알림.

6. 서버가 **데이터**를 클라이언트에게 전송. PSH 플래그가 설정되어 있으므로, 클라이언트는 이 패킷을 즉시 처리해야 함을 의미.

7. 클라이언트가 서버의 데이터를 받았음을 확인하는 ACK 패킷을 전송.

8. 서버가 HTTP 200 OK 응답과 함께 HTML 문서를 전송.

9. 클라이언트가 서버의 HTTP 응답을 받았음을 확인하는 ACK 패킷을 전송.

10. 클라이언트가 더 이상 데이터를 전송할 것이 없음을 알리는 FIN-ACK 패킷을 전송.(4way-1)

11. 서버가 클라이언트의 FIN 패킷을 확인하고, 자신도 더 이상 전송할 데이터가 없음을 알리는 FIN-ACK 패킷을 전송.(4way-2,3)

12. 클라이언트가 서버의 FIN 패킷을 확인하는 ACK 패킷을 전송. 이로써 TCP 연결이 완전히 종료.(4way-4)

### tcp 소켓을 끊을때 뭔가 이상한데?

1. 왜 FIN이 아니라 FIN ACK을 보내지?(10번라인)

소켓클로즈시 유실 패킷이 있는지 없는지 알리는차원에서 마지막 ACK의 ack=number를 다시한번 FIN과 함께 보내는 전략으로 half close를 방지하려하기때문

<img width="681" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/2239913d-9f82-4241-926f-92eb640fb32c">



2. 3way인데? (2way, 3way 가 한번에 날라감, 11번라인)

성능상의 이유로 실제로 이렇게 구현된 경우가 많다고함

<img width="1011" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/ff9c5e19-48ab-4fe2-8a62-099efd3fe23f">


# TIME_WAIT 소켓의 문제점

4way에서는 연결을 먼저 끊으려는쪽과 끊음 당하는쪽으로 분류된다.

- 즉 active와 passive가 존재.

4way시 각각의 tcp state를 다시 알아보면

- 1way: active closer는 FIN 을 날리고 FIN_WAIT1 상태가 됨, 
- 2way: passive closer는 FIN을 받으면 CLOSE_WAIT이 되고 ACK을 날리며 이를 수신한 active closer는 FIN_WAIT2
- 3way: passive closer가 FIN을 날리며 LAST_WAIT
- 4way: active closer가 fin을 받으면  ack을 보내고 일정시간 TIME_WAIT(느린세그먼트를 위한 임시 대기)

> TIME_WAIT 상태는 일반적으로 2MSL(Maximum Segment Lifetime, 세그먼트의 최대 생존 시간) 동안 유지
> RFC 793에서는 이 값을 2분으로 제안

즉 active closer 입장에서 FIN을 보내고 상대의 FIN을 받고 ACK을 보낸 뒤에도 일정시간 대기상태에 빠진다.

만약 tps가 10000인 상황이라면 10초만에 10만개의 timewait 소켓이 쌓이게되는데 일반적으로 하나의 ip당 6만개의 포트가 할당가능하므로 고갈이 일어나게된다.
이를 방지하기위에 커넥션 풀같은걸 쓰는것!

그럼 이런 고갈을 방지하려면 어떻게해야할까?

## 클라이언트 사이드라면 - 서버입장에서 호출도 당연 클라이언트다

### net.ipv4.tcp_tw_reuse

커널 파라미터로 TIME_WAIT 소켓을 재사용하게하여 고갈방지가능

### 커넥션풀 사용
db, redis, aws client 커넥션풀 등등을 생각하면 쉬움

## 서버사이드라면

서버사이드에서 active closer가 되는 가장 쉬운방법은 keepalive_timeout

<img width="695" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/c6e88185-d5ad-48b1-8bd6-4c6b6fcb0645">

NGINX에서 http keepalive_timeout 설정을 0으로 변경해두고 curl을 통해 요청을 날려보자

<img width="700" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/b56e061c-b160-4312-a309-9ce88a46f6ef">

서버사이드에 TIME_WAIT 소켓이 있는걸 발견!

tcpdump를 보면

<img width="1498" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/98f1ca88-944e-4eb5-af77-bc61d1ccb636">

fin이 한번밖에없는데?

<img width="790" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/09795fa8-c2b1-4a7a-a699-428b7d9a64ce">

http응답 패킷의 헤더에 connection: close라는 헤더가 내려오며 먼저 연결을 끊어버리는것을 알 수 있다!(로그가 뭔가 누락된건가?)

그렇다면 해결법은?

### net.ipv4.tcp_tw_recycle
서버입장의 소켓재사용 파라미터
BUT 절대 설정하지말것!

syn 패킷 드랍현상이 발생할 위험이 있음!

### keepalive 사용하기
http라면 keepalive를 쓰자

### 실무적으로?
NGINX를 리버스프록시로 앞단에 두고 뒤에 앱서버를 두는경우가 많은데 이때 앱서버가 keepalive가 없을경우 NGINX는 항상 앱서버와 TCP 커넥션을 맺고 닫을것이기때문에 불필요한 성능 낭비가 일어난다.





