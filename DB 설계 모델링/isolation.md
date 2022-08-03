# isolation이란?

> 독립성(Isolation)은 트랜잭션을 수행 시 다른 트랜잭션의 연산 작업이 끼어들지 못하도록 보장하는 것을 의미한다. 
> 이것은 트랜잭션 밖에 있는 어떤 연산도 중간 단계의 데이터를 볼 수 없음을 의미한다. 
> 공식적으로 고립성은 트랜잭션 실행내역은 연속적이어야 함을 의미한다. 
> 성능관련 이유로 인해 이 특성은 가장 유연성 있는 제약 조건이다.

- 모든 요청을 전부 직렬화시킨다면, 한번에 하나의 트랜잭션밖에 수행하지 못하므로 그만큼 성능에 제약이 발생할 수 밖에 없으며, 이를 조율하기위해 isolation level이 존재

# isolation level

트랜잭션간 고립수준을 얼마나 둘것인가에 대한 정의

- READ UNCOMMITTED
- READ COMMITTED
- REPEATABLE READ
- SERIALIZABLE

## READ UNCOMMITTED
A트랜잭션이 데이터 변경을 가질때, 아직 커밋됨과 상관없이 다른 트랜잭션이 해당 변경을 읽어내는 레벨
즉 가장 낮은 수준의 격리(isolation) 레벨을 의미

### trouble case
- A트랜잭션이 특정 데이터 컬럼을 ++ 쳐서 `3` 이됨
- 아직 커밋 전
- B트랜잭션이 그 특정데이터를 조회
- `3` 으로 조회됨

=> dirty read

만약 A트랜잭션이 문제가 발생해 rollback 한다면?
B트랜잭션은 `3` 을 가지고 이미 트랜잭션쿼리를 수행하기때문에 데이터 정합성에 큰 문제가 생김!

권장 x

## READ COMMITTED
- 커밋된 트랜잭션을 다른 트랜잭션이 읽는 고립수준
- 가장 일반적인 격리 레벨
- 같은 트랜잭션 내에서 같은 select을할때 다른 값이 나오는 부정합이 발생할 위험이 존재(`NON-REPETABLE READ` 부정합)

### trouble case
- A트랜잭션에서 select 으로 count가 3
- B트랜잭션에서 count를 4로 만들고 commit
- A트랜잭션에서 select으로 count를 조회하니 4가되는 부정합 발생

비즈니스 로직의 정합성 중요성에 따라 문제가 될 수 있음!


## Repetable Read

- 트랜잭션이 시작되기 전에 커밋된 내용에 대해서만 조회
- 거의 완전한 고립레벨
- 트랜잭션에 시퀸셜한 고유 번호(id)를 가지고 자신보다 이후 트랜잭션에서 먼저 commit이 발생할때, select이 이후 일어날경우 undo영역에 백업된 데이터를 불러와 커밋 이전 영역을 재참조
- 성능상 하위 레벨과 크게 차이는 안남


### trouble case 1 - update 부정합
- 1번트랜잭션이 select 으로 count 3 조회
- 2번트랜잭션이 select 으로 count 3 조회
- 1번트랜잭션에서 count 3 일때 4로 update
- 2번 트랜잭션이 count 3 일때 4로 update -> 0 affected

### trouble case 2 - Phantom Read
A트랜잭션중 B트랜잭션에서 특정 데이터가 insert되고 이를 A트랜잭션에서 update 치는경우 A트랜잭션에서 이후부터 select이 되는 현상

## Serializable
가장 단순하고 엄격하게 모든 트랜잭션을 순차적으로 발동
