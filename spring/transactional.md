# Spring에서 @Transacntional 사용했을 때 Default 격리 레벨은?
![](https://user-images.githubusercontent.com/45676906/143460038-bab3d62e-4b82-4473-97c4-0aa32d5bb1d8.png)
- DB의 기본 isolation level을 사용
- mysql의 default isolation level은 InnoDB기준 `REPEATABLE READ`

- 따라서 phantom read 문제가 발생할수 있음
- 필요에 따라 serialize 레벨 설정이 필요할때가 있다

# @Transaction 속성

|속성|설명|예시|
|-|-|-|
|isolation|Transaction의 isolation Level. 별도로 정의하지 않으면 DB의 Isolation Level을 따름|
|propagation|트랜잭션 전파규칙을 정의 , Default=REQURIED|
|readOnly|해당 Transaction을 읽기 전용 모드로 처리 (Default = false)|
|rollbackFor|정의된 Exception에 대해서는 rollback을 수행|
|noRollbackFor|정의된 Exception에 대해서는 rollback을 수행하지 않음|
|timeout|지정한 시간 내에 해당 메소드 수행이 완료되지 않은 경우 rollback 수행. -1일 경우 no timeout (Default = -1)|



# references 
https://github.com/jinia91/TIL/blob/master/DB%20%EC%84%A4%EA%B3%84%20%EB%AA%A8%EB%8D%B8%EB%A7%81/isolation.md
