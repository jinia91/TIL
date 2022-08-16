중복여부를 결정하는 기준은 코드가 변경에 반응하는 방식이며, 변경해야 할 이유가 같다면 두 코드는 중복이다.

코드 모양이 비슷하다고 코드의 중복이라고 생각해서는 안된다!

변경이유가 같은것이 코드의 중복!

dry 원칙, Once and Only Once 원칙, 단일 지점 제어 원칙(Single Point Control)


(타입 코드) 를 사용하는 클래스는 낮은 응집도, 높은 결합도의 문제를 시달리게됨

타입 코드는 필연적으로 타입에 따라 사용하지 않는 필드를 가지게 되고, 사용하지 않는 메서드를 가지게 되며, 이는 낮은 응집도, 그리고 여러 타입에 따른 다양한 의존성을 하나에 모이게 되면서 높은 결합도를 가지게 됨

요구사항과 구현의 차이가 클수록 코드를 이해하기가 힘들어진다

요구사항은 유즈케이스 -> 코드는 비즈니스 로직을 담는것이 근본적인 목적 -> 비즈니스로직과 구현이 차이가 날수록 직관성에서 멀어지고, 코드를 이해하기가 더 어려워짐 -> 상속은 부모클래스와 자식클래스가 강결합되어있으므로, 자식클래스를 사용하는 비즈니스로직이 부모클래스의 코드제약에 제한받게 되고, 코드가 복잡해짐 -> 요구사항과 구현이 차이가 생기고 이는 코드를 이해하기 어려워짐
 

## 취약한 기반클래스 문제(Fragile Base Class Problem, Brittle Base Case Problem)


> 상속을 위한 경고 1
    > 자식 클래스의 메서드 안에서 super참조를 이용해 부모클래스의 메서드를 직접 호출할 경우, 두 클래스는 강하게 결합되므로 super호출을 제거할수 있는 방법을 찾아 결합도를 제거하라


> 상속을 위한 경고 2
> 상속받은 부모 클래스의 메서드가 자식 클래스의 내부 구조에 대한 규칙을 깨뜨릴수도 있다.


> 상속을 위한 경고 3
> 자식 클래스가 부모클래스의 메서드를 오버라이딩할 경우 부모 클래스가 자신의 메서드를 사용하는 방법에 자식 클래스가 결합될 수 있다.


> 상속을 위한 경고 4
> 클래스를 상속하면 결합도로 인해 자식 클래스와 부모클래스의 구현을 영원히 변경하지 않거나, 자식 클래스와 부모 클래스를 동시에 변경하거나 둘중 하나를 선택할 수 밖에 없다.



상속과 합성의 가장 큰 차이점은 상속은 부모클래스를 컴파일시점에 참조하지만, 합성은 런타임시점에 참조가능하다는것!

즉 코드단위에서는 참조를 상위 추상화에 하고, 런타임시점에 구현체에 의존하게하므로서 결합도를 낮출수 있다.

-> 상속은  whiteBox Reuse
-> 합성은  blackBox Reuse
[GOF DP]



믹스인 -> 다중 상속 -> 컴파일시점에 다중상속하기!



### 합성은 조합을 통해 불필요한 클래스 생성을 방지할수 있음



## 다형성의 CS적 정의


![첨부 이미지](https://jinia-img-bucket.s3.ap-northeast-2.amazonaws.com/7e4955bf-8439-4e23-9de2-d39b47fece3d.png)



- 제네릭 프로그래밍
- 서브타입 다형성
- 오버로딩 다형성
- 강제 다형성 -> 언어차원에서 지원해주는 다형성



## 올바르게 상속을 사용하기 위한 조건

1. 상속관계가 is-a 모델링을하는가
2. 클라이언트 입장에서 부모 클래스의 타입으로 자식클래스를 사용해도 무방한가
    - 리스코프원칙을 준수하는가
    - 행동 호환성의 문제

실무적인 관점에서 2번을 통해 체크하는것이 훨씬 이해하기 쉬움

is-a 새 - 펭귄

새는 날수 있는데 펭귄은 못남 ㅇㅇ

is-a를 단편적으로, 글자 그대로 받아들이면 자연어의 모호함에 빠져 오개념을 가질수 있음

is-a는 적절하지 못하다!

클라이언트 입장에서 행동호환이 되는가, 동일 메시지 -> 클라이언트가 문맥에 맞는결과를 항상 얻을수 있는가

인터페이스는 결국 클라이언트가 기대하는 바에 따라 분리되어야한다!

=> 이것이 곧 `ISP`


인터페이스를 나누는 기준은 client 관점에서 생각하는것이 실무적이고 유용한 판단!

객체지향이 현실을 그대로 코드로 옮긴다던가, 자연어에 대한 모호함에 기대며 이해하는것은 OOP에 대한 잘못된 접근법


> 클라이언트와 격리한채로 본 모델은 의미있게 검증하는 것이 불가능하다

어떤 모델의 유효성은 클라이언트 관점에서만 검증가능한것

LSP 위반은 잠재적인 OCP 위반



클라이언트 - 서버와의 관계는 협력을 의무와 이익으로 구성된 계약관점에서 계약에 의한  설계(`DBC`) 라고 칭하기도함

d!

결국 클라이언트의 문맥에 맞는 결과를 얻는다는것은 상속 여부를 해당 타입을 사용하는 문맥-도메인-비즈니스에 강결합하여 생각해야하고

문맥에 따른 검증은 테스트코드를 통한 비즈니스 명세로 정의하는것이 좋을듯?
