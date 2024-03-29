# 데이터베이스는 세부사항이다
## 중요한것은 데이터
- 데이터
- 물리 데이터 관리 시스템 == DBMS e.g) Mysql, redis, mongoDB
- DBMS 접근 기술 e.g) Java JPA, JDBC, R2DBC 등등
- 애플리케이션
- 도메인

여기서 데이터와 도메인이 가장 중요하고 DBMS ~ DBMS접근기술 or 애플리케이션까지는 변경가능한 infra 기술이라 볼 수 있다

## DBMS의 기술이 애플리케이션과 도메인을 오염시키지 않게 할것!
언젠간 변할수 있다

# 웹은 세부사항이다
프리젠터 영역은 언제든 변경가능
- jsp쓰는 방식에서 restApi로 변경된거처럼
- restApi에서 이벤트 드리븐방식의 messaging 시스템으로 변경될수 있는것처럼

이때 프리젠터 영역이 핵심 업무 규칙과 완전히 격리된다면 생산 리소스가 훨씬 적게들것이다

# 프레임워크는 세부사항이다...?!
- 프레임워크는 침투적 특징을 가진다
- 스프링이 이런 침투성을 많이 제했다곤하지만... 실제론 그래도 다양한 코드안에 스프링 의존성이 생기기마련
- 제품이 성숙해졌을때 프레임워크가 제공하는 기능과 틀을 벗어날 일이 있을까? 프레임워크가 변경될 일이 있을까? 버전업은 존재할듯

## 업무객체는 절대 스프링에 대해 알아서는 안된다! : 라고 주장
- 메인 컴포넌트에서 스프링을 사용해 의존성을 주입해주는방향을 제안
- 이러려면 결국 업무 컴포넌트(core)에서 모든 객체를 조립해주는 Factory 클래스를 만들고 해당 클래스의 인스턴스를 Main에서 빈으로 등록하는 방식으로 구현하는게 클린아키텍처스러운 구조일듯

# 사례연구 : 비디오 판매
## 1. 유스케이스 분석
### 액터 뽑아내기
- 제작사
- 관리자
- 구매자
- 시청자

해당 애플리케이션을 사용할 액터는 크게 4가지

![image](https://user-images.githubusercontent.com/85499582/223097355-ef8b1e89-ce18-4508-a918-1ecfbf1803ea.png)


### 액터가 행할 유즈케이스 정의하기
- 추상 유스케이스 : 범용적인 정책
- 다른 유스케이스에서 이를 더 구체화하기

### 컴포넌트 아키텍처
- 이때 각 컴포넌트는 단일 .jar 파일 또는 단일 .dll파일에 해당하지만 반드시 나눌필요는 없다. 타협하자

### 핵심
- 단일책임 원칙에 기반한 액터의 분리! : 변경 사유
- 의존성 규칙 : 저수준 -> 고수준


# 대중적 아키텍처 정리

## 계층기반 레이어드 아키텍처
- 직관적이고 러닝커브가 낮지만, 업무 규칙 업무 도메인에대해 아무런 규약이 없기때문에 앱이 커질수록 복잡해짐

## 기능기반 패키지
- 도메인기반으로 수직으로 패키징을 나누기
- 이때 DIP를 사용해 의존성 방향도 제어

## 포트 어댑터
- 내부 도메인과 외부 인프라를 구분하기
- 기능기반 패키지에서 기술영역과 도메인을 명확히 분리하기
- 
## 컴포넌트 기반 패키지
- 핵심은 결국 레이어를 무너뜨리는 코드가 점점 추가된다는것
- 모듈화는 강한 컨벤션으로 작동하게되어 장기적으로 유지보수에 유리
- 컴포넌트 기반 패키지 아키텍처의 가장 큰 이점은 주문 관련된 무언가를 코딩해야할 때, 오직 한곳 즉 OrdersComponent만 둘러보면 된다는점!

