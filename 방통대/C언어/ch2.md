# 자료형과 선행처리기
## 상수와 변수(C언어 자료형 알아보기)
### 상수
- 항상 고정된 값을 갖는 자료
- 값이 한번 정해지면 프로그램 도중 그 값을 변경할 수 없는 수
#### 종류
- 정수형 상수 : 10진수, 8진수, 16진수로 표현
 <img width="608" alt="image" src="https://user-images.githubusercontent.com/85499582/233767542-4fc64229-a9c1-4947-a60d-e66b133b3845.png">
  
- 실수형 상수 : 부동소수점 형 상수, double형을 기본 자료형으로 사용
<img width="693" alt="image" src="https://user-images.githubusercontent.com/85499582/233767570-849032e2-4568-4da4-8a16-225ba80c9519.png">


- 문자형 상수 : 단일인용부호로 묶여 있는 1개의 영문자나 숫자 문자
  - 단일인용부호 ''  
  - 내부적으로는 해당 문자의 asc코드값이 사용
  - escape 문자
  - <img width="577" alt="image" src="https://user-images.githubusercontent.com/85499582/233767607-bfa27927-95d3-4129-9c27-23a83d7596c4.png">

- 문자열 상수
  - 이중인용부호"" 로 묶여있는 복수개의 영문자나 숫자
  - 기억공간에 보관될 때는 문자열 끝에 null문자 \0가 자동으로 추가
  - <img width="705" alt="image" src="https://user-images.githubusercontent.com/85499582/233767688-6a6e814e-71c5-4333-b7d5-df78e400cb07.png">

### 변수
> 변할 수 있는 값
> 프로그램 실행 도중 변할 수 있는 값이 저장되는 기억공간 자체를 의미, 기억공간을 정의
- 수시로 변경될 수 있음!

#### 특징
- 모든 변수는 이름이 있다
- 모든 변수는 정해진 자료형이 있다
- 모든 변수는 할당된 값을 갖는다
- 반드시 사용전, 선언이 되어야한다

## C언어 자료형
### 자료형 종류
<img width="698" alt="스크린샷 2023-04-22 오후 3 54 43" src="https://user-images.githubusercontent.com/85499582/233768148-814b3029-e470-423e-a08c-b718faab449a.png">

#### 정수형
- 운영체제에 따라 표현범위가 조금씩 다를 수 있음

<img width="612" alt="스크린샷 2023-04-22 오후 3 56 41" src="https://user-images.githubusercontent.com/85499582/233768223-9cfdeb65-f38d-46ce-910e-4e109690dd63.png">

#### 실수형

<img width="614" alt="스크린샷 2023-04-22 오후 3 57 40" src="https://user-images.githubusercontent.com/85499582/233768271-556e90f9-ec5d-43dc-8df9-6feab776f223.png">


#### 문자형
- asc로 표현

<img width="569" alt="스크린샷 2023-04-22 오후 3 58 16" src="https://user-images.githubusercontent.com/85499582/233768315-c544ecfc-9293-4da4-9d67-d902f1b26ebe.png">

<img width="572" alt="image" src="https://user-images.githubusercontent.com/85499582/233768391-8660663d-2db5-41ac-921a-42a049291f4e.png">

#### 열거형
- 숫자 대신 단어를 사용
- enum 태그명 {열거자1, 열거자2 ...}

<img width="657" alt="스크린샷 2023-04-22 오후 4 01 33" src="https://user-images.githubusercontent.com/85499582/233768407-a434fe29-85ea-470d-920c-94497a7153d1.png">

<img width="592" alt="image" src="https://user-images.githubusercontent.com/85499582/233768860-137981e2-ff3f-4f37-8f61-49f5ad7c6429.png">

- 초기화 안해도 default로 1일 들어가네?

<img width="436" alt="image" src="https://user-images.githubusercontent.com/85499582/233768947-d2f23295-daee-424e-b327-046ca4ac0328.png">

- 초기값에 int 넣어서 인덱싱 시작 번호를 조절가능

## 선행처리기(preprocessor)
- 컴파일에 앞서 프로그램 선두에 선언된 지시자들을 미리 처리하는 역할을 수행

<img width="634" alt="스크린샷 2023-04-22 오후 4 13 04" src="https://user-images.githubusercontent.com/85499582/233769159-e0d12454-dadf-4f0e-b6ee-f1982c322929.png">

### 주의점
- 반드시 # 으로 시작
- ; 안붙임
- 한줄에 하나의 명령만
- 소스 프로그램의 첫부분에 위치

### 파일포함
> #include
- c언어에서 제공되는 헤더파일('*.h')를 자신의 소스파일에 읽어 들여 함께 컴파일하고자할때 사용
- 예를 들어 입출력하려면 stdio.h 를 #include해야함!
#### 형식 : 
- `#include <파일명>`
- `#include "파일명"`
- - `#include "\tc\lib\파일명"` 디렉토리 탐색시 "" 로 사용하면 됨

### 매크로 정의
> #dfine

- 선행처리기 define을 사용하여 단순 치환되는자료
- 프로그램 작성 시 에 명령이나 수식 또는 상수값이 자주 사용될때 이들을 대표하는 이름을 붙여 사용하는 대상
- 상수나 함수 둘다 정의가능

#### 형식
- `#define 매크로명 자료` `#define IP 123.12312.123` 전역선언스러운느낌
- `#undef 매크로명` 정의 해제

#### 함수정의 형식
- `define 매크로명(인수) (수식)`
- `define 매크로명(인수, 수식) (수식)`

단순 치환방식이므로 전달 인자의 자료형을 명시할 필요가 없고, 또 어떠한 자료형 변수를 인자로 전달해도 잘동작, 속도도 훨씬 빠름

<img width="478" alt="image" src="https://user-images.githubusercontent.com/85499582/233769569-7257afd2-2e4a-4ff5-ae5a-cfd355dc6cf9.png">

### 조건부 컴파일
> #if, #else, #elif, #endif
- 성능향상을 위해

<예시>
<img width="731" alt="스크린샷 2023-04-22 오후 4 22 06" src="https://user-images.githubusercontent.com/85499582/233769650-0b520bc7-08b5-4ee6-8e87-e8738cf6d135.png">

컴파일 자체를 하고말고를 정할수 있다.








