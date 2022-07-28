
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
 일반적인 array 데이터 조회가 빠르고, 중간에 데이터 삽입시 성능문제
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
 


# 추가로 더 알아보기
- redis Persistence(RDB, AOF)
- redis Pub/Sub
- redis Stream
- 확률적 자료구조
  - hyperloglog
- redis Module

# reference
- https://www.youtube.com/watch?v=mPB2CZiAkKM


