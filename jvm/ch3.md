# GC를 공부해야하는 이유
- 다양한 메모리 오버플로와 누수문제를 해결해야하는 상황
- 더 높은 동시성을 달성하는데 GC가 방해가 되는 상황
- 적절히 모니터링하고 조율할수 있어야하기떄문

# 죽은 객체 판단
## 참조 카운팅 알고리즘
- 객체를 가리키는 참조 카운터를 추가, 참조하는곳이 늘어날때마다 ++
- 참조하는곳이 하나 사라질때마다 카운터 값을 1씩 감소
- 카운터 값이 0이 된 객체는 더는 사용할 수 없음

- CPython은 O, 자바는 X
- 순환차조 문제 풀기 어려움 : 단둘이 서로 참조하고있다면 사실상 두 객체는 쓸모없는 객체들이지만 아무튼 참조 카운터 1

## 도달 가능성 분석 알고리즘
- GC루트라고 하는 루트 객체들을 시작 노드로 삼고 시작노드부터 DFS로 도달 못하는 객체만 삭제
### GC루트 대상
- 가상머신 스택에서 참조하는 객체 : 실행중인 메서드에서 쓰인 매개변수, 지역변수, 임시변수 등
- 메서드 영역에서 클래스가 정적 필드로 참조하는 객체 : 자바 클래스의 참조 타입 정적 변수
- 메서드 영역에서 상수로 참조되는 객체 : 문자열 테이블 안의 참조
- JNI가 참조
- jvm 내부에서 쓰이는 참조
- syncronized로 잠겨있는 객체
- 자바 가상 머신 내부 상황을 반영하는 JMXBean

## 참조 개념
- 강한 참조 : 전통적인 정의의 참조. 프로그램 코드에서 참조를 할당
- 소프트 참조 : 유용하지만 필수는 아닌 객체. 캐싱캐념. 메모리 오버플로가 나기 직전에 2티어 회수에서 회수될 대상으로 SoftReference클래스
- 약한 참조 : 소프트 참조보다 낮은 티어의 참조로 다음번 GC까지만 사는 대상. WeakReference 클래스
- 파이널 참조 : finalize 호출시 대기열큐에 들어가는 경우. 해당 큐에서 참조는 하고있으니 아무튼 참조
- 팬텀 참조 : 대상 객체가 회수될때 알림을 받기위한 용도로 사실상 참조로 취급안함. PhantomReference 클래스

## 실제 죽었는지 살았는지 판단 과정
- 알고리즘으로 도발 불가능판단이 되면 1차 마킹
- 마킹된 객체들은 finalize 호출 대상인지 필터링 - 이미 호출했는지
- F큐라는 대기열에 추가
- 대기열 큐 내에서 만약 다시 참조가 되면 부활
- 부활한 경우에도 다시 도달 불가능 판단되면 이때는 finalize호출 없이 바로 삭제

> 즉 finalize는 객체 삭제라기보단 삭제 대기열에 추가이며 일종의 사형선고같은 개념. 살아나도 다시 도달불가능이 되면 그냥 강제 삭제됨.

```java
package com.jvm;

class FinalizeEscapeGC {
  public static FinalizeEscapeGC SaveHook = null;

  public void isAlive() {
    System.out.println("살아있음");
  }

  @Override
  protected void finalize() throws Throwable {
    super.finalize();
    System.out.println("삭제중");
    SaveHook = this;
  }

  public static void main(String[] args) throws InterruptedException {
    SaveHook = new FinalizeEscapeGC();

    SaveHook = null;
    System.gc();
    Thread.sleep(500);
    if (SaveHook != null) {
      SaveHook.isAlive();
    } else {
      System.out.println("주금 ㅠ");
    }

    SaveHook = null;
    System.gc();
    Thread.sleep(500);
    if (SaveHook != null) {
      SaveHook.isAlive();
    } else {
      System.out.println("주금 ㅠ");
    }

  }
}
```

<img width="376" height="117" alt="image" src="https://github.com/user-attachments/assets/2ee2926d-9db4-4ebc-a997-d1d2237cd07e" />

unreachable 2번 되면 finalize는 더 호출되지 않고 바로 삭제


## 메서드 영역
- 상수와 클래스가 회수 대상
  - 이 클래스으 ㅣ인스턴스가 모두 회수됨
  - 이 클래스를 읽어 들인 클래스 로더가 회수됨
  - 이 클래스에 대핟ㅇ하는 java.lang.Class 객체를 아무곳에서도 참조하지 않고 리플렉션기능으로 이 클래스의 메서드를 이용한느곳도 전혀 없음


# GC 알고리즘

## 세대 단위 컬렉션 이론

0 
  




