# IAM
> IAM : Identity And Management
- 글로벌서비스

## Root User & Users
- 오직 계정을 만들때만 사용해야하고 루트계정은 사용해서도 공유해서도 안된다
- 하나의 사용자는 조직내의 한사람에 해당
- 필요하다면 사용자들을 그룹으로 묶을 수 있음

## Grouping
- 유저는 여러 그룹에 속할 수 있다

## Permissions
- 유저나 그룹에 권한 할당 가능
- Json으로 작성하면된다
- 최소권한의 원칙

<img width="787" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/e25941f8-20fc-470f-9b9b-ae31c091f09b">


## IAM 정책
- 그룹 정책 : 그룹에 해당하는 정책
- 인라인 정책 : 유저 개인에 해당하는 정책

### 정책 구조
- json
  version, id, statement(sid, effect(Allow, Deny), principal, action, resource, condition) 으로 구성됨

|||
|-|-|
|Version|policy language version|
|id|policy id|
|Statement|사실상의 정책|

- statement 구조
|sid|id|
|effect|Enum allow, deny|
|principal|어디에 적용할지?|
|Action| 허용/거절 행위들 목록 |
|Resource|어떤 리소스일지|

## MFA - Multi Factor Authentication

> aws는 유저의 비밀번호 정책을 다양하게 커스텀 가능, 그중에서도 아주 강력한 정책이 MFA

- virtual MFA device
- U2F Security Key
- Hardware key

  == otp 같은거

<img width="1142" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/0b3a811a-e1d5-4eb5-a22e-98a988f85dd3">

  

