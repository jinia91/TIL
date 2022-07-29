
# redis 소개
- in-memory data structure store
- open source
- support data structures
  - strings, set, sorted-set, hashes, list
  - hyperloglog, bitmap, geospatial index
  - stream

# cache 사용이유 목적
- 나중에 요청된 결과를 미리 저장해 재사용하기위함
- dp에서 메모라이제이션하는것도 일종의 캐싱
- cpu의 캐시도 캐시
  - l1 캐시, l2 캐시, l3, 메모리, 디스크

## 캐시는 어디서 사용하는가?
<img width="713" alt="스크린샷 2022-07-28 오후 10 36 16" src="https://user-images.githubusercontent.com/85499582/181518692-ae7ef8a7-8167-485d-b207-40f2c639b55c.png">

- 파레토 법칙에따라 전체 요청의 80%는 20%의 사용자에 의한케이스가 많고, 전체 데이터의 20%가 주로 조회됨을 고려할때 전략적으로 어떻게 캐싱해야할지 그림을 그려볼수 있음

- 1. 일반적인 실무 사용 케이스 `look aside cache pattern`

<img width="686" alt="스크린샷 2022-07-28 오후 10 38 15" src="https://user-images.githubusercontent.com/85499582/181519109-7561db04-e9fd-4b7c-b914-0f5f5fe401aa.png">

- 2. 쓰기가 빈번한 데이터를 선캐싱 이후 배치로 db에 동기/persist 화 `write back pattern`

<img width="656" alt="스크린샷 2022-07-28 오후 10 39 39" src="https://user-images.githubusercontent.com/85499582/181519429-e2323916-ad63-4e2f-ac05-628de771e2f4.png">

배치에 동기화이전 캐싱서버가 날라가면 데이터 유실 위험성이 존재

## redis는 그럼 보통 실무에서 어디서 사용할까
- remote data store
  - 서버간 데이터를 공유하고 싶을때(a,b,c... 서버간)
- 만약 한대의 서버에서만 필요하다면 전역변수를 쓰면되지않을까?
  - redis자체가 atomic을 보장
- 주로 사용하는곳
  - 인증 토큰 저장(string, hash)
  - ranking 보드로 저장
  - 유저 api limit

# redis의 개발 편의성 사례 - 랭킹서버 구현시
## 개발 편의성
- 빈번하게 바뀌는 랭킹을 db에서 데이터를 다 sorting하여 매번 불러오기엔 부담, hdd i/o 를 생각할때 성능문제
- redis sorted set을 이용하면 랭킹을 구현할 수 있음
- 덤으로 replication도 가능
- 다만 가져다 쓰면 거기의 한계에 종속적이 됨
  - 10명 1kb
  - 10000명 1mb
  - 천만건 1gb
  - 10조건 1tb  사실 돈만있다면 스케일자체는 가능
- redis는 자료구조가 atomic하기 때문에 race condition을 일반적으로 피할수 있음

# collection supported by redis
- strings
 일반적인 키밸류 
- list
 중간에 데이터 삽입시 성능문제
 spring security oauth redistokenstore 라이브러리 이전버전이 해당 자료구조를 썻는데 데이터 삽입/ 삭제에서 성능이슈가생겨서 set으로 
 스택구조나 리스트 구조를 사용한다고 생각하면되고 lpush rpush 혹은 lpop rpop으로 데이터 insert
- set
  중복값 x
  sadd key value를 넣을때 value가 이미 존재한다면, 추가되지않음
- sorted set
  정렬된 set
  redis쓸때 많이쓰게됨
  zadd key score value 로 insert하고 value가 이미 있으면 score에 기록
  - score 값이 double 타입인데 js는 54비트 이상의 큰수를 표현시 근사치로 표현하면서 정확한 값이 표기안되는 문제가 있는데, 웹 통신간 문제가 발생할 여기가 있음
- hash
 key 안에 subkey가 존재
 
## 주의점
- 하나의 컬렉션안에 너무 많은 아이템 담지 않기
- 만개 이하

# redis 운영
## 메모리관리를 잘하자
- redis는 인메모리 데이터 구조
- 물리메모리 이상 사용할경우 당연히 문제가 됨
- swap설정을 해두었다면 swap이 발생하여 hdd i/o발생, 성능 극단적인 저하 인메모리 캐시를 쓰는이유가 없어짐
- swap이 없다면 OOM으로 죽어버림
- maxmemory 옵션시엔 제한 메모리 이상 사용시 랜덤하게 데이터를 삭제
- redis는 사용 메모리가 정확히 얼마인지 알수없음 jemalloc의 한계
- 모니터링이 필수
- redis 모니터링을안한다면 swap이 일어나고있는지조차 모를수도 있음 ㅠ.ㅠ
- 레디스는 하나의 큰 메모리 단위로 쓰기보단 더 작은 단위로 쓰는게 좋음
  - fork를 하게될때, write가 헤비하다면 copy on write로 일시적으로 1.5배~2배까지 메모리사용이 일어남
  - 만약 서버 메모리가 64gb고 레디스 64gb짜리 서버를 띄우고 있다면 fork시 일시적으로 메모리사용량이 증가하면서 물리 메모리 이상을 점유할 필요가 생길수 있고 이때 swap 이 일어나거나 oom이 터질 위험존재
  - 따라서 작은 인스턴스를 여러개 띄우는게 더 안전함
- 메모리 파편화도 고려

## 메모리가 부족하다면?
- 70% 이상 사용시 마이그레이션을 고려해야함
- 있는 데이터 줄이기


### 메모리를 줄이는 설정
- 자료구조의 구현체 선택시 내부적으로 ziplist 를 선택하면 메모리 사용이 절약됨
- 인메모리라 애초에 풀서치가 빠르므로, 최적화 없이 선형탐색을 사용하는 방법으로 2~30% 메모리 절약가능
- 성능적으론 데이터가 많을시 문제되므로 결국 원래 자료구조로 변경되도록 설정해야함

## O(n)관련 명령어 주의하자
 
- redis는 싱글스레드

> 일반적으로 10만 tps 까지 소화가능

- 반대로 고려하면 단건 트랜잭션이 엄청 느리게되면 9만9천건의 다른 트랜잭션이 지연되면서 서버 병목 발생

따라서 redis내에서 o(n) 명령은 되도록 피하자!

### o(n) 명령 예시

- keys
  - 모든 key 순회
  - 사용하지말고 scan을 사용할것!(페이징으로 가져올수있으므로 훨씬 가벼움)
- flushall, flushdb
  - 어쩔수없이 쓸수도있음
- delete collections
  - 백만개 삭제시 1~2초 걸림
- get all collections
  - 10만개 데이터를 매번 가져온다고 생각하면 매우 느림
  - 다 가져와야하는상황이 있을경우 쪼개서 가져올것 자체적으로 페이징처리을 하려고해보자

# Replication
- Async Replication
  - Replication Lag 이 발생 가능(마스터엔 있는데 slave엔 데이터가 없는 상황, 클러스터기반 aws rds사용하는 실무에서 실제로 겪어봄)
- Replicaof(>=5.0) or 'slaveof' 명령으로 설정가능
  - Replicaof hostname port
- DBMS로 보면 statement replication 가 유사
## Replication 설정 과정
  - secondary에 replicaof or slaveof 명령 전달
  - secondary는 PRIMARY에 sync 명령 전달
  - primary는 현재 메모리 상태를 저장하기 위해
    - fork(만악의 근원)
  - fork한 프로세서는 현재 메모리 정보를 disk에 dump
  - 해당 정보를 secondary에 전달
  - fork 이후의 데이터를 secondary에 계속 전달

## 주의할 점
- fork가 발생하며 이는 현재 사용하는 메모리의 1.5~2배까지 점유율이 늘어날수있음을 감안해야함
- 엘라스틱캐시 redis는 fork없이 replication 가능할수 있음! doc 제대로 볼것
- 많은 대수의 redis 서버가 replica를 두고있다면 네트웍 이슈나 사람의 작업으로 동시에 replication이 재시도 되도록 하면 문제가 발생할수 있음

# redis 권장 설정!
- Maxclient 설정 50000
- RDB/AOF 설정 off
- 특정 commands disable
  - keys
  - aws의 elastic cache는 이미 하고 있음
- 전체 장애의 90% 이상이 keys와 save 설정때문
  - 적절한 ziplist 설정 필요

# Redis 데이터 분산
## 데이터 분산 방법
- app에서 분산
- redis cluster
## consistence hashing
redis에 고유 해시코드를 지정하고 index 해시코드의 근사치값들을 저장시키는 전략으로 rebalancing이 최소화할수 있음

# sharding
> 데이터를 어떻게 나눌것인가? 데이터를 어떻게 찾을것인가?

## Range
- 그냥 특정 범위만큼 쪼개기
- 서버에 부담이 불규칙하게 분배됨

## MODULAR
- N % K 로 서버의 데이터를 결정
- Range보다 데이터를 균등하게 분배할 가능성이 높음

## Indexed 서버
- 일종의 티켓서버를 두고 균등하게 redis서버에 데이터 분배
- SPOF

# Redis Cluster
- 장점
  - 자체적인 Pri, sec, failover
  - slot 단위 의 데이터 관리
- 단점
  - 메모리사용량이 더 많음
  - 마이그레이션 자체는 관리자가 시점을 결정해야함
  - library 구현이 필요

# Redis Failover
## Coordinator 기반
- zookeeper, etcd, consul 등의 Coordinator 사용
- 헬스체크로 current redis 저장

## VIP 기반

가상 ip기반으로 접속중 헬스 체크로 확인해서 장애시 secondary를 primary로 승격시키고 vip를 secondary에 할당(라우팅)

## DNS 기반

vip와 동일한 방식, 도메인변경

결론적으로 vip,dns 모두 클러스터 엔드포인트를 본다고 생각하면 편함

# Monitoring Factor

- Redis Info 통한 정보
 - RSS(물리메모리 사용량! 무조건 모니터링!)
 - Used Memory(redis가 생각하는 메모리사용량)
 - Connection 수(커넥션 맺고 끊기를 자주하면 성능 문제가 있음!, 잦은 커넥션 생성 종료로직은 안좋다)
 - tps 수치(cpu에 부담)
## CPU 100%칠경우
- 처리량이 매우많다면? 스케일업
- o(n) 명령이 많은경우
  - 패턴을 파악하여 전략적으로 명령을 수정하던지 


- System
  - CPU
  - Disk
  - Network rx/tx 

# 결론
- 기본적으로 redis는 좋지만, 메모리를 빡빡하게 쓸경우 관리가 어려음
- write가 heavy할때는 특히 요주의


# 추가로 더 알아보기
- redis Persistence(RDB, AOF)
- redis Pub/Sub
- redis Stream
- 확률적 자료구조
  - hyperloglog
- redis Module

# reference
- https://www.youtube.com/watch?v=mPB2CZiAkKM


