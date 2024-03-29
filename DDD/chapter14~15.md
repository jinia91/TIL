# 14. 모델의 무결성 유지
## Bounded context

- 애플리케이션은 여러 모델을 가지고 있음
- 도메인의 모델은 문맥상에서 존재하며, 문맥 외부에서는 다르게 인식되거나 사용될수 있음

> 모델이 적용되는 컨텍스트를 명시적으로 정의하는것이 장기적인 애플리케이션 유지보수 관점에서 더 좋다.
> 경계 내에서 모델을 엄격하게 일관되 상태로 유지하고 경계 바깥의 이슈때문에 모델이 오염되지 않도록 격리해라

### 문맥을 제대로 정의하지 않고 모델을 제대로 정의하지 않을경우

- 중복된 개념을 가진 모델이 여러개 생성될 위험성
- 허위 동족 언어(같은 용어이나 다른 개념)이 발생할 위험성

## Continuous Integration

- 다수의 개발자들이 동일 Bounded Context상에서 작업함을 상상해보면, 모델의 단편화는 피하기 어려움, 그렇다 하더라도 시스템을 더 잘게 쪼개게되면, 결국 가치있는 수준의 통합과 응집성을 잃는 결과를 초래할 수 있음
- 따라서 이를 방지하기위해, Continuous Integration을 하여 모델 개념의 통합과 구현수준의 통합을 지속하고 수정 발전해나갈 필요가 있다.

### CI 프로세스
- 단편화가 발생시 이를 빠르게 알려줄수 있는 단계적이고 재생 가능한 병합/ 빌드 기법
- 자동화된 테스트 스위트
- 수정사항이 통합되지 않은 상태로 존재할 수 있는 시간을 적당히 짧게 유지하는 규칙(작은 서브태스크단위로 빨리 pr, 머지하기!)

## Context Map
> 하나의 애플리케이션 안에서 context로 분리된 만큼, 서로 다른 Context 간에는 필연적으로 의존성과 관계가 생길수밖에 없다. 만약 이를 적절히 정의해두지 않는다면 경계는 흐려지고 각각의 Context 가 서로 스며들어 강결합될 위험이 있다.
> 따라서 적절한 정의가 필수이며, 이 영역을 잘 표현하는 지도(map)을 작성해라

- 이떄 map안에 그려진 context는 유비쿼터스언어로 된 명확한 이름이 제시되어야 하고 경계지점과 경계지점의 특성을 명확하게 표현해야한다.

- 만약 map을 만들다가 문제가 발생한다면? 작성을 멈추고 해당 균열을 해결하기위해 여러 패턴을 적용하거나 수선작업을 진행해라
  - 이 때 이 작업은 일부 bounded context 내로만 제한

## Shared Kernel pattern

- bounded context는 기본적으로 완전히 분리되고 transtlator를 통해 필요한 영역만 소통하고 관리되는것이 바람직하지만, 조직의 구조적, 물리적한계나 리소스의 문제, 혹은 높은 결합도로 이것이 어려울수 있음
- 이때 사용하는것이 바로 Shared Kernel

### 공통 라이브러리, 공통 모델, 공통 커널 만들기

- 도메인의 모델과 로직을 공유하는 공통 커널 구현하기
- 한번 만들어진 shared Kernel은 되도록 변경되지 않아아햠!
- 하위 시스템간으 통합을 용이하게 만드는것이 목표

## Customer / Supplier 
> 컴포넌트간의 관계가 일방적인 스트림일경우 두 컴포넌트 개발팀간의 관계 설정을 C/S로 설정하기

- 상류팀이 하류 시스템을 망가뜨릴지도 모른다는 두려움 없이 개발이 되고, 하류 팀이 지속적으로 상류팀을 감시하지 않고도 자신의 작업에 집중할 수 있게 자동화된 테스트 스위트가 존재해야함!
- 일반적으로는 shared Kernenl로 구현함이 타당할것이나, 만약 서로 다른 기술로 구현된경우라면? 이럴때 대체할수 있는 패턴이 바로 C/S
- 조직 정치와 관련된 내용인듯...?

## Conformist(준수자)

## AntiCorruption Layer

> 개념적객체와 행위를 하나의 모델과 프로토콜에서 다른 모델과 프로토콜로 변환하기 위한 메커니즘

- 일반적으로 외부 시스템에서 사용하는 의미체계를 단 하나의 컴포넌트가 책임지고 번역하는것은 쉽지 않은 일
- 우리의 모델과점에서 응집력 있는 책임을 맡는 여러개의 serivice가 이 역할을 수행하는것이 바람직


### Facade
- 대안 인터페이스, 최상위 인터페이스
- Facade는 기저 시스템의 모델을 변경하지 않음!

### Adapter
- 번역 계층, 어댑터 패턴에서의 어댑터


### 결국은 Bounded Context 분리와 경계 유지를 위한 결합도 level의 차이와 구현 수단들

- 강결합 Shared Kernal <-> 약결합 AntiCoppruption Layer 정책 결정과 요구사항의 필요성에 따라 결정할것! -> Separate Ways

![image](https://user-images.githubusercontent.com/85499582/189602903-7d9428bc-67aa-4790-9f94-8e124d5e8df2.png)


# Distilation

> 혼합된 요소를 분리해서 본질을 좀더 값지고 유용한 형태로 뽑아내는 과정

## Core Domain 과 Generic SubDomain 의 분리

- 가능한 작게, 하지만 가장 변동이 적고 비즈니스 가치에 핵심이 되는 부분을 Core Domain으로 분리하고 인력 배치에 힘쓸것(hr 관점)
- SubDomain에 대해서는 외부솔루션, 외주등의 방법도 고려



## E.G

<img width="631" alt="스크린샷 2022-09-12 오후 5 32 12" src="https://user-images.githubusercontent.com/85499582/189608592-a72ea7ae-0476-4289-8593-878560c0700c.png">


- as-is : 하나의 통합된 해운 시스템 + 결제 모듈


<img width="619" alt="스크린샷 2022-09-12 오후 5 33 00" src="https://user-images.githubusercontent.com/85499582/189608736-772fd1f5-84d2-4eb8-bd2a-3cedaf2b1ad7.png">

- to-be : core domain 인 Delivery와 분리된 sub-domain들 

## advanced Core Domain - abastract core

- 심층 모델을 디스틸레이션하여 가장 핵심이 되는 core domain을 고도화하는것이 가치있는 도메인모델을 만드는가장 확실한 방법
- 

