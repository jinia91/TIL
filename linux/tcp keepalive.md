# TCP Keep alive 개념

> 3way handshake 후 fin을 통해 연결을 끊지 않고 빈 패킷을 타이머마다 보내며 해당 세션을 계속 유지

- `netstat -napo`

<img width="222" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/8c08d0f9-0c55-4bd0-88bf-4af8d40397d0">

`SO_KEEPALIVE` 옵션을 통해 보통 keep alive를 킴

- keepalive 패킷은 대략 68바이트정도로 아주작기때문에 지속적인 통신이 필요하다면 키는게 바람직하다.

# TCP keepalive의 파라미터들
`sysctl -a | grep -i keepalive`

<img width="341" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/04bdfd9e-a0e7-4384-acb3-b242bc935884">

- net.ipv4.tcp_keepalive_time: 이 파라미터는 TCP 연결이 어느 정도의 시간동안 어떠한 데이터도 주고받지 않은 상태에서 첫번째 keepalive 프로브를 보내기까지의 시간(초)을 설정한다.

- net.ipv4.tcp_keepalive_probes: 이 파라미터는 첫번째 keepalive 프로브 이후에 얼마나 많은 keepalive 프로브를 보낼 것인지를 설정한다. 만약 이 많은 프로브들 중 하나라도 응답이 없다면, 그 때 연결은 종료한다. 

- net.ipv4.tcp_keepalive_intvl: 이 파라미터는 keepalive 프로브 사이의 간격(초)을 설정한다.

# TCP Keepalive 좀비 커넥션

- keepalive의 가장 강력한 효과는 좀비 커넥션 방지

## 좀비 커넥션?

- tcp 커넥션은 여러가지 이유로 fin을 받지 못한채로 연결이 끊길수 있음
- 커넥션 관리자체가 os단에서 이루어지므로 물리적인 이유, 패킷유실등의 이유가 존재, 또한 애플리케이션단에서의 커넥션도 마찬가지 개념으로 os단에서의 커넥션 끊김을 확인 못한채 좀비상태로 존재할 수 있음

## keepalive면?

좀비 커넥션 발생시 keepalive 패킷의 probe 수만큼 체크후 커넥션은 자동 종료된다.

**즉 keepalive는 연결계속 유지를 하는 기능이라기 보단, 연결이 계속 유지되는지 체크를 위해 polling하는 역할만 하는셈!, 응답이 없으면 자동 종료할지언정, 연결을 계속 유지하는 기능은 아님!**

# http keepalive vs tcp keepalive

 - 무연결성을 지향하는 http이지만 http1.1 부터 기본 활성화 상태
 - 하지만 해당 기능의 개념과 역할은 약간 다르므로 명확히 알아두자.

## 개념
- tcp 세션이 연결된후, 그 위에 http프로토콜로 데이터가 전송하고 도착하면 http keepalive에 따라 tcp 연결을 유지
- 새로운 http 요청이 있으면 해당 tcp 세션을 재 이용한다는 의미


## 케이스로 이해하자!
- http keepalive = 60
- tcp keepalive time =10, probe =5, interval = 5

1. 3way로 tcp 커넥션 연결
2. http request
3. http response
4. 10초 후 probe가 가서 ack 체크 x 5
5. 60초가 되면 http 요청을 보냈던 애플리케이션은 http 커넥션에 keepalive 스펙에따라(60초) 커넥션 종료명령
6. tcp 레이어에서 4way 로 종료

tcp keepalive는 tcp 커넥션 연결 지속성을 보장하는게 아니다!
http keepalive도 해당 시간만큼 tcp 세션을 유지하겠다는 의미


# 로드밸런서 DSR 혹은 Inline일경우 좀비커넥션 이슈

<img width="912" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/34c7ffeb-e466-4e21-87d4-b19119deedfd">
- DSR 방식

- 만약 리버스 프록시를 사용한다면 요청 응답을 각각 server client 관점에서만 바라보면 된다. 하지만 dsr 방식이면 이야기가 다르다.

## DSR 로드밸런서 케이스

- 로드밸런서는 세션 매핑 테이블만 가진 바이패스이며, idleTimeout이 존재

- 만약 클라이언트가 http keepalive가 5분인경우, 그리고 LB의 idleTimeout이 120초라면

1. 클라이언트 -> LB 3way
2. LB는 클러스터중 하나의 인스턴스에 3way 전달하고 세션 매핑
3. 서버의 응답은 클라이언트로 다이렉트로 전달
4. 이후 2분동안 추가 요청이 없음
5. LB는 idleTimeout으로 세션 테이블에서 해당 데이터 제거
6. 3분대에 클라이언트가 http keepalive 되어있는 소켓으로 요청
7. LB가 다른 인스턴스로 해당 http 요청을 전달
8. 해당 인스턴스는 클라이언트와 3way를 맺지 않았으므로 tcp out되는 소켓도 없음
9. 따라서 RST를 서버로 보냄
10. 클라이언트는 이과정에서 장애를 겪거나 타임아웃
11. 원래 클라이언트와 세션을 맺었던 서버는 위의 과정을 모르므로 좀비 커넥션상태로 계속 존재


## 이럴때 tcp keepalive!
- 120초 안에 tcp keepalive probe 패킷을 




