## 1. 아파치 카프카가 무엇이냐?

data in motion platform 
움직이는 데이터를 처리하는 플랫폼, 이벤트 스트리밍 플랫폼

이벤트 :
비즈니스에서 일어나는 모든일(데이터)를 의미
웹사이트에서 무언가를 클릭
청구서 발행
송금
배소물건의 위치정보
택시의 gps좌표
센서으 ㅣ온도/ 압력 데이터

이벤트는 빅데이터의 특징을 가짐
비즈니스의 모든 영역에서 광범위하게 발생
대용량의 데이터 발생

연속적인 많은 이벤트의 흐름



특징

이벤트 스트림을 안전하게 전송
publish & subscribe
이벤트 스트림을 디스크에 저장
write to disk(가장 큰 특징!)
이벤트 스트림을 분석 & 처리


사용 사례

Event 가 사용되는 모든곳에서 사용
messaging System
IOT 디바이스로부터 데이터 수집
앱 로그 수집
Realtime Event Stream Processing(이상 감지 등)
DB 동기화(분리된 DB간 동기화) - 대표적으로 고객정보처럼 쪼개진 정보를 쪼개진 db에서 쓸경우 데이터 정합성은 어떻게?
카프카로 해결 가능!
실시간 ETL
빅데이터 기술과 같이 사용도 가능


카프카가 rabbit MQ에 비해 훨씬 성능이 좋다고함
-throughput 의 경우 20배, 레이턴시도 훨씬 낮음



아파치 카프카 vs 컨플루언스 카프카 

두가지가 존재

컨플루언스 카프카 엔터프라이즈는 유료



## 사용사례

시스템 모니터링에도 사용가능
메시지 허브로서 사용도 가능	



## 2. 아파치 카프카의 주요 요소

### 1. topic

kafka 내에서 메시지가 저장되는 장소, 논리적인 표현

Producer : 메시지(event)를 생산해서 Kafka 의 Topic으로 메시지를 보내는 애플리케이션
Consumer : Topic의 메시지를 가져와서 소비하는 애플리케이션
Consumer Group : Topic의 메시지를 사용하기 위해 협력하는 Consumer들의 집합

여기서 핵심은 Producer와 Consumer간의 의존관계는 존재하지 않음!
메시지 브로커인 kafka가 브로커 패턴으로서 두 애플리케이션을 연결시켜주는것!

Commit Log : 추가만 가능하고 변경 불가능한 Kafka 내의 자료구조, publisher의 event가 write
데이터는 항상 로그 끝에 추가되고 변경되지 않음


Producer는 Kafka 내의 Commit Log 라는 공간에 write하며, 
Consumer는 Kafka 내의 Commit Log를 read



토픽은 논리적인 단위일뿐 물리적 구분은 x

카프카는 토픽을 물리적으로 partition으로 쪼갬

Partition : Commit Log, 하나의 TOPIC은 하나이상의 Partition으로 구성, 병렬처리를 위해 다수의 파티션이 존재할 수 있음
Segment: 파티션 내의 더 세부적인 단위

### 주요 특징 정리
Topic 생성시 Partion 개수 지정하며 개수 변경은 가능하나 운영시에는 변경 권장 xxx	
파티션 번호는 0부터 시작하고 오름차순
topic 내의 파티션들은 서로 독립적임
event 위치를 나타내는 offset 이 존재하며, offset은 파티션 내에서만 의미가 있음, 파티션을 나누는것 자체가 병렬연산을 위해서이므로, 병
병렬처리중 시퀸셜한 의미를 가지진 못함
offset은 커밋로그 자료구조이므로 증가만할뿐


## 주키퍼, 브로커

카프카의 주요 구성요소는

여러개의 주키퍼 + 여러개의 브로커

브로커란 :
 파티션에 대한 read / write를 관리해주는 소프트웨어
Kafka server라고 부르기도 함
토픽 내의 Partition들을 분산, 유지및 관리 해주는 솔루션
각각의 Broker들은 id로  식별
중요한것은 토픽의 일부 파티션만 포함할뿐 topic != broker

브로커중 하나는 Controller라는 Role을 부여받음
컨트롤러는 주키퍼를 통해 broker liveness를 모니터링
leader와 replica 정보도 클러스터내의 다른 broker들에 전파
리더가 죽을경우 leader 선출 역할을 함
컨트롤러가 장애시 주키퍼가 컨트롤러 재선출

Kafka Cluster : 여러개의 Broker들로 구성됨

Client는 특정 브로커에 연결되면 전체 클러스터에 연결


카프카 클러스터는 최소 3대 이상의브로커로 구성되는것을 권장!!! 안전성을 담보하려면 4대이상 쓰길!

모든 카프카 브로커는 Bootstrap서버라고 불림

하나의 브로커에만 연결해도 전체 브로커에대한 리스트를 클라이언트에게 반환해줌(각 브로커는 모든 브로커리스트를 알고있다- 메타데이터)
그러면 클라이언트는 브로커리스트를 통해 필요한 브로커로 찾아가게됨



주키퍼란?
	브로커를 관리하는 소프트웨어(Broker들의 목록 / 설정을 관리)
변경사항을 kafka에 알려줌 topic 생성/제거, Broker 추가 / 제거 등
주키퍼없이 카프카는 동작 불가능
하지만 최신버전 KIP-500을 통해 주키퍼 없이 동작하는 카프카 버전도 릴리즈 예정(2022)
홀수 서버 갯수로 동작되도록 설계(최소 3, 권장 5)
Leader = writer / Follower = reader
분산형 설정 정보 유지, 분산 동기화 서비스 제공하고 대용량 분산시스템을 위한 네이밍 레지스트리를 제공하는 소프트웨어
분산작업을 제어하기위해 tree형태의 데이터 저장소를 사용
주키퍼를 사용하여 멀티 kafka broker들간의 정보공유, 동기화 등을 수행하는 역할
주키퍼 앙상블
주키퍼가 홀수인 이유는  Quorum 알고리즘 기반이기 때문
설정정보를 전파하는데 항상 과반수 방식으로 의사결졍을 내리기때문에 홀수갯수가 필요 -장애발생시
3대나 4대나 과반수를 생각하면 어차피 2대 장애시 동작안하는건 똑같음, 따라서 홀수가 효율적





## Producer 세부

Message == record == event == data

카프카는 producer 의 메시지를 byte Array로만 저장
파티셔너를 세부 설정가능, 보통은 디폴트로 하지만, 알고리즘을 자체 구현도 가능



## Consumer 세부

컨슈머가 커밋 로그를 읽는 방식

컨슈머가 읽어야할 topic을 읽은 경우(Topic-partition0:5)
Topic__consumer__offsets 라는 내부 Topic에 ConsumerGroupName:Topic:파티션id:커밋로그위치 로 저장
컨슈머 그룹의 컨슈머들은 내부 로직에 따라 파티션을 균일하게 분배받고 작업량도 균등하게 분배받도록 되어있음



메시지 ordering(순서 보장)

병렬처리에서 순서보장은 대체 어떻게하지?

하나의 토픽 내에 여러 파티션이 존재하게되면 사실 전체 토픽의 순서보장은 불가능함

만약 파티션이 한개라면? 순서보장은 당연히 가능 하지만 처리량 저하

모든 메시지의 순서 보장이 비즈니스상 반드시 필요한가?

대부분의 경우 key로 구분할 수 있는 메시지들의 순서보장으로 족함
그리고 카프카 default 파티셔닝 알고리즘은 key에따라 동일 파티션에 데이터가 저장되는 구조이므로

key로 sorting된 이벤트에 대한 순서성은 기본적으로 보장됨 -> 멀티 파티셔닝 가능!

하지만 운영중에 파티션 개수를 변경하면 알고리즘이 꼬여서 순서 보장이 불가능해짐!

따라서 운영중에 파티션 개수는 변경하지말것

작업량의 균등 분배를 위해 키설계가 중요



만약 컨슈머가 장애가 나는경우?

컨슈머 리밸런싱이 일어나서 장애가 난 컨슈머가 바라보던 partition의 처리를 다른 컨슈머가 추가로 도맡아 하게됨




## 브로커 장애가 나는경우?

브로커가 장애가나면 브로커 내의 파티션들을 못쓰게되는데 이때 파티션 내의 커밋로그 내역들은 어쩌지?

-> replication 으로 극복

파티션을 복제해서 장애를 대비

다른 브로커들은 자신이 도맡은 파티션 이외 다른 브로커의 파티션들도 replica로서 동기화하여 계속 저장

Master- slave 처럼 Leader - follower 로 불림

Replication Factor 설정!

복제는 하지만 기본적으로 Read/Writer는 Leader로만 바라보며, Follower는 어디까지나 장애 대응용

하지만 카프카 최신 버전에서는 

Consumer의 경우 Follower를 통해서도 read가 가능해졌다고함(옵션이 존재)

leader가 한 파티션에만 몰리는 문제(disk hotspot risk)를 방지하기위해 rebalance가 default이며

주기적으로 모니터링하는 옵션도 존재

leader.imbalance.check.interval.seconds: 300s
leader.imbalance.per.broker.percentage: 10 (10%이상 파티션의 처리량이 차이나면 경고?)


ISR.  - 얼마나 복제를 잘하고있는지 지표

ISR이 높은 Replica 가 차기 Leader 후보

만약 ISR을 replica.lag.max.messages로 판단할경우 , 순간적인 트래픽 급증으로 OSR이 발생하여 불필요한 
error 발생,불필요한 retry를 유발할 수 있음

따라서 replica.lag.time.max.ms 로 판단하는것이 더 좋다!


브로커가 isr 을 관리


High Water Mark
가장 최근에 커밋된 메시지의 offset 추적
replication-offset-checkpoint 파일에 체크포인트를 추적

Leader Epoch
새 리더가 선출된 시점을 offset으로 표시

컨슈머는 committed 된 메시지만 읽을수 있으며, committed는 High Water Mark가 찍힌 지점까지를 의미하고
High Water Mark는 ISR Replica가 들고있는 메시지까지를 의미함	 




카프카 아키텍처를 구성하는데 참조할 Doc

컨플루언스 공식 doc
https://www.confluent.io/resources/apache-kafka-confluent-enterprise-reference-architecture/?test=hushlylp&var=original

권장사항

브로커는 분리된 각각의 전용서버에 설치 권장
Replication Factor는 broker 갯수만큼 설정가능
Mission Critical Topic에는 RF 보통 3개
브로커는 4개이상권장
Min.insync.replicas 도 2이상 권장


# kafka connect 란?

시스템간 메시지 전송을 해주는 app을 개발할것인가?

예를들어 카프카랑 db랑 연결은 어떻게해?, 카프카랑 s3랑은? 하둡은?

source connect
sink connect

kafka connect 
	카프카 안팎으로 데이터를 스트리밍하기 위한 framework
	다른 데이터 시스템을 카프카와 통합하는 과정을 표준화한 framework
	통합을 위한 connector 개발 배포 관리를 단순화
connectors
태스크를 관리하여 데이터 스트리밍을 조정하는 플러그인, jar
Tasks
데이터 전송 구현체 instance
workers
커넥터 및 태스크를 실행하는 실행중인 프로세스
Converters
커넥트와 데이터를 보내거나 받는 시스템간의 데이터 변환에 사용되는 컴포넌트
Transforms
메시지 변환 컴포넌트


kafka schema Registry

	스키마 정의, 중앙집중식 관리를 위해 사용하는 프레임워크

	
	AVRO
		아파치 오픈소스 프로젝트중 하나
		데이터 serialization을 제공
		데이터 구조 형식
		바이너리이므로 효율적으로 저장 serialize 시스템



kafka Streams
이벤트 스트리밍용 라이브러리
자바로 가능
스트리밍처리하기 매우 쉽다!
KsqlDB
이벤트 스트리밍 DB, sql 엔진



카프카 기반 event stream Processing 3가지 방식

카프카 publish subscribe
카프카 스트림스
Sql DB


## EDA
분산 시스템에서 비동기 통신 방식으로 이벤트를 발행 / 구독하는 아키텍처

비동기 통신 사용 => 느슨한 결합도로 모듈간 커뮤니케이션 가능
edm에서 발생한 이벤트는 이벤트 스토어에 저장(이벤트 로그)
트랜잭션 관리 : retry, rollback
동기통신의 전제 : peer to peer 가 반드시 살아있어야하고 서로 알아야함 => 복잡도 증가
	




