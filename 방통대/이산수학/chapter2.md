# 명제
> 참과 거짓을 구별할 수 있는 문장이나 수학적 식

- 명제의 진리값 T/F
## 명제의 종류
- 합성명제
- 조건명제, 쌍조건명제
- 항(상)진(리인)명제, 모순명제

- `X + 2 = 0` : 명제 함수

# 논리 연산
- 합성명제란? : 논리 집합안의 논리 변수(명제)를 논리 연산자를 이용해 논리 상수로 표현하는것, 논리 연산식
  - p V q
  - 하나 이상의 명제와 논리연산자 그리고 괄호로 이루어진 명제

## 논리합(disjuction; or, v)
- p V q
<img width="412" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/43bb69ab-411e-4d09-bb75-023d30b8ddfe">

## 논리곱(conjunction; and, ^)
- p ^ q
<img width="423" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/e480b6ca-5dc6-4fab-abd6-a31d12d55c32">

## 부정(negation; ~, ㄱ)
- ~p

## 배타적 논리합(exclusive or; xor, ⊕)
- p⊕q = (p ^ ~q) v (~p ^q)
  - 하나는 참, 하나는 거짓인경우
<img width="595" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/f55f4c18-509e-4e0e-aeae-bfe9a4553fa2">

## 조건 명제(conditional proposition, ->)
- 명제 p와 q가 있을때, 명제 p가 조건의 역할을 수행하고 명제 q가 결론의 역할을 수행하는 경우
- p -> q(p => q)
- p는 q의 충분 조건
- q는 p 의 필요 조건

<img width="286" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/f7ffa1ab-97de-4457-b0a7-a881e3d2e12d">

## 쌍조건명제(conditional proposition, <->)
- 명제 p 와 q 가 있을때 명제 p와 q가 조건의 역할과 결론의 역할을 동시에 수행하는 경우
- p <-> q (p <=> q)
  - (p -> q) ^ (q -> p)
<img width="327" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/9befb2dc-9412-4964-b23f-302060c266e4">


## 논리적 동치 (logical equivalence, =)
- 두 명제 p와q가 논리적으로 동등할때 논리적 동치라고하고, p = q로 표시한다
- 논리적으로 동등하다는 말은, 두 명제가 항상 동일한 진리값을 가진다는 의미
- p <-> q


## 동치
- 역, 이, 대우
<img width="526" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/74c825c6-d5b0-49b0-bf9d-eb20b4187d3b">
<img width="489" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/26ad5a0e-cbb8-4321-9309-c6b199fa728c">

### 논리적 동치법칙
<img width="430" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/78994546-e3ed-4672-93b8-a3d10dae8d8c">
<img width="408" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/9f6a051d-f7de-42f8-9ac2-4269800acaea">
<img width="522" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/b24e8b41-947e-4cb6-abcc-03a3e841521a">
<img width="519" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/bb7a9d8c-13eb-41be-9ae0-fe12f056180d">
<img width="431" alt="image" src="https://github.com/jinia91/TIL/assets/85499582/d8a4b3c5-c1c4-4897-9014-1fd74c9ac4a2">

## 술어논리와 명제함수
### 명제함수
> 변수의 값에 의해 함수의 진리값이 결정되는 문장이나 식

- 변수의 명세 방법은 적시하거나 한정하거나 두가지 방법이 있음

### 한정화

- 전체 한정자 : 전체 한정자는 모든, 또는 임의의 를 의미하며 명제함수와 같이 사용되었을 경우에는 정의역의 모든 x에 대해 p(x)가 참임을 의미한다.
- 존재 한정자 : 존재 한정자는 존재한다를 의미하며, 명제함수와 같이 사용되었을 때는 정의역의 어떤 x에 대해서 p(x)가 참임을 의미한다.

### 명제함수의 타당성
- 벤다이어그램, 삼단논법

# 추론
- 참으로 알려진 명제를 기초로하여 다른 명제를 유도해 내는 과정을 추론이라고 한다
- 결론의 근거를 제공하는 알려진 명제를 전제라고 한다.
- 새로 유도된 명제는 결론

## 유효추론
- 유효추론은 전제를 참이라고 가정하였을 때, 결론이 항상 참이 되는 추론

 ## 추론규칙
- 기본 추론규칙은 논리적 동치를 이용함
 - 선언적부가
 - 단순화
 - 긍정논법
 - 부정논법
 - 선언적 삼단논법 또는 소거
 - 가설적 삼단논법 또는 추이






