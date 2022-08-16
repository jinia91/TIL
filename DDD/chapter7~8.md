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

![KakaoTalk_Photo_2022-08-16-23-34-53](https://user-images.githubusercontent.com/85499582/184906602-bd796c9b-9114-4395-b32a-f60b58ac3fa3.jpeg)
> 양방향 연관관계보다는 중간에 해소하는 엔티티를 통해 순환 참조를 해소하는 방향으로 설계하자
> VO는 자신의 소유자를 참조해서는 안된다! JPA의 Embeddable 타입를 생각해보자
> Location 같은 엔티티는 실무에서 Zone을 생각해보자

- 순환참조는 항상 동기화를 유지해야하는 점때문에 장기적인 유지보수관점에서 추천 x 꼭필요한 경우에만 하자


### 4. AGGREGATE의 경계
- 어그리거트는 생각보다 작은 범위에서 이루어져야함
- 추가적으로 어그리거트 경계간 엔티티참조시에는 간접참조(id)를 지향하자. OOP에는 어긋날수 있어도 MSA를 고려할때 보다 유연한 설계가된다

### 5. 객체 생성 factory패턴의 구현
- 컬렉션으로 엔티티를 참조하는것은 OOP스런 구현이긴하나, 유지보수관점에서 베스트프랙티스로 볼수는없음
- id기반 질의를 통해 DB에 의존을 하더라도 느슨하게 연관관계를 맺는것이 더 유연한설계

### 6. 패키징방법
- 모듈단위 패키징
- 유비쿼터스 언어에 기여할수 있는 분할방법을 택할것


> Service라는 네이밍을 모두 Service라 짓지말고, 역할에 따라 구분하여 컨벤션을 만들어보자





