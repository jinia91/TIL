# 컴포넌트란?
  > 배포 가능한 최소 단위

- .jar로 말수있는 최소 단위
- 모듈이 모여서 컴포넌트가 된다. 모듈 < 컴포넌트

# 컴포넌트 응집도
## REP : 재사용 릴리스 등가 원칙 (Reuse/Release Equivalence Principle)
> 재사용 단위는 릴리즈 단위와 같다

- 단일 컴포넌트는 응집성 높은 클래스들과 모듈들로 구성되어야함
- 하나의 컴포넌트로 묶인 클래스와 모듈은 반드시 함께 릴리스 할수 있어야한다
  - 해당하는 상황이 존재하나?

## CCP : 공통폐쇄 원칙 (component closure principle)

- SRP 와 동일
- 변경이 요구될경우 하나의 컴포넌트만 수정해야한다. 만약 여러 컴포넌트가 같은 목적으로 수정되고 있다면 두 컴포넌트는 하나의 컴포넌트여야할 확률이 높다.

## CRP : 공통 재사용 원칙 (component reuse principle)

- CCP의 반대 접근
- 같은 사유로 변경될 모듈들(혹은 Class)을 한 컴포넌트에 넣어야한다는 의미는, 반대로 응집도 없는 강하게 결합되지 않은 컴포넌트들은 별도의 컴포넌트가 되어야한다는 의미!
  - common의 저주!
    - 사내 서버 컴포넌트가 5개이고 모두 Common이라는 공통 컴포넌트를 의존하고 있다고 가정할때, a서버의 요구사항으로 common 특정코드의 변경이 필요하다 가정하자
    - 해당 코드는 b 서버에서 사용하고 있는 상태
    - 즉 cde는 해당 코드를 사용하고 있지 않음에도 common의 버전업 릴리즈에 끌려 재배포를 해야한다

- ISP와 동일원리
- 컴포넌트는 다양한 PUBlic interface를 제공하고 이 interface는 변경 사유에 맞게끔 찢어져야 한다.

> 필요하지 않은것에 의존하지마라 

## 컴포넌트 균형 다이어그램

![image](https://user-images.githubusercontent.com/85499582/216039617-ea194173-bdd8-4315-a10c-87495e815a57.png)

- REP CCP는 포함원칙
- CRP 는 배제 원칙
- 프로젝트 초기라면 CCP가 더 중요 : 빠른 개발엔 재사용성이 중요하기 때문
- 하지만 프로젝트가 성숙하고 그 푸로젝트로부터 파생된 또다른 프로젝트가 늘어날수록 유지보수가 더 중요해진다! 

## 핵심은 재사용이 아니라 유지보수다!
- 재사용은 유용하지만, 유지보수는 자익적 생산성의 저하를 낳는다. 재사용을 위한 코드가 유지보수를 저해한다면 재사용을 포기하고 중복을 선택하는것이 더 바람직!

# 컴포넌트 결합
> 컴포넌트 사이의 관계를 설명하는 원칙

## ADP : 의존성 비순환 원칙
> 컴포넌트 의존성 그래프에 순환이 있어서는 안된다

- 내가 의존하는 코드가 변경되면 내코드 동작안해요 ㅠ
### sol : 주단위 빌드, 정기 integration
- 스프린트 주기를 해침
- 권장하지 않음

### 순환의존성 제거하고 CI 달성

### 하향식 설계(top-down)는 불가능
- 앱 -> 컴포넌트 -> 클래스 순으로 설계하는것은 직관적이지만, 옳은 방법이 아니다.
- 앱이 어떻게 변경되고 진화할지는 아무도 모르는것이며, 컴포넌트를 분리하는 이유는 유지보수 높은 재사용을 하기 위함이고, 유지보수를 위해서는 CCP를 파악해야하는데, 초기 프로젝트는 이를 잘 알지 못하기때문
- 이런 성급한 컴포넌트 분리는 의존성 순환을 가져올확률이 높다

## SDP : 안정된 의존성 원칙

- 설계는 정적일수 없고 변경은 불가피
- 변경이 쉽지 않은 컴포넌트가 변동ㅣ 예상되는 컴포넌트에 의존하게 만들어서는 절대로 안된다
- 의존하는 컴포넌트는 불안한 컴포넌트이며 의존받는 컴포넌트는 안전한 컴포넌트
- '안전' 이 좋은걸 의미하는게 아님

> 안전보다는 동적 컴포넌트, 정적 컴포넌트 같은 용어가 더 좋지않을까?

- 다이어그램에 표현할경우 관례상 동적 컴포넌트는 위에, 정적 컴포넌트는 아래
- 의존성 방향이 이상하거나 문제가 된다면! DIP를 쓰자! == 추상컴포넌트?!

## SAP : 안정된 추상화 원칙
> 컴포넌트는 안정된 정도만큼만 추상화되어야한다










