# 언어의 사용(확장 예제로 학습하기) - 메모

## 화물 해운 시스템을 DDD로 구현해보기

### 1. 모델링

- N개의 customer - 1개의 cargo , customer는 여러 역할로 배분 : 다대일(cargo가 1)
- cargo는 배송 목표가 존재
- specification을  충족하는 여러 carrier Movement가 합쳐져서 배송 목표가 달성

> Specification 패턴을 사용하기(9장에서 학습)

### 2. 도메인 격리 

- 도메인의 책임이 시스템의 다른 부분과 섞인느것을 방지하고자 레이어드 아키텍쳐를 사용


### 3. Entity and VO 구분하기 

> 핵심은 식별성

- Customer는 당연히 Entity
- Cargo는?  당연히 Entity
- HandlingEvent ? 
  - 개별적인 이벤트 사건으로 처리상황을 알아낼수 있으므로 Entity?

- Location
  - 내부적인 식별자를 가진 독자적인 위치(해운시스템의 경우)
  - 만약 배송시스템이라면 Address는 고유의 주소로 볼 수 있으므로 역시나 entity로 관리하는게 맞을듯?

- Delivery History : Cargo와 1대1이므로 VO로 봐야하나?
- Delivery Specification : VO

- 시간 날짜 역할등은 VO





