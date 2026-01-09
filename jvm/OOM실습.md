# 자바 힙 오버플로
- 메모리 해제 안되면서 계속 객체 생성하면 OOM
- 무한루프 로직을 잘못짰을때 흔히 발생, 실무에서도 봤다
- 힙덤프 찍어보면 손쉽게 확인 가능

```java
public class Main {
  public static void main(String[] args) {
    var list = new java.util.ArrayList<Object>();
    while(true){
      list.add(new Object());
    }
  }
}
```

<img width="1197" height="26" alt="image" src="https://github.com/user-attachments/assets/eba9f530-a681-4418-892b-8c0330dd3214" />

- 메모리 누수 or 오버플로우 인가? => 해당사항은 메모리 누수

<img width="912" height="243" alt="image" src="https://github.com/user-attachments/assets/20266214-7c76-4968-b465-149726265843" />

# jvm스택과 네이티브 메서드 스택 오버플로우
- 재귀함수에서 흔히 발생
- 너무 많은 지역변수 선언시 이론적으로는 오버플로우 가능

```java
public class Main {
  private int stackLength = 1;
  public void stakLeak() {
    stackLength++;
    stakLeak();
  }

  public static void main(String[] args) {
    Main main = new Main();
    try {
      main.stakLeak();
    } catch (StackOverflowError e) {
      System.out.println("Stack length: " + main.stackLength);
      e.printStackTrace();
    }

  }
}
```

<img width="554" height="222" alt="image" src="https://github.com/user-attachments/assets/fac6d7c2-3c83-4c8a-9e85-6725995ec3ab" />

- 너무 많은 수의 스레드를 만들어 메모리 오퍼플로우가 날수도있음
  - 이경우는 사실상 물리메모리의 부족일확률이 높으므로 최대 힙크기와 스택 용량을 줄여야함

# NIO dm 오버플로우
- 다이렉트 메모리 사이즈보다 그 이상으로 할당할경우 OOM이 나지만 힙덤프에 표현 안됨
- 실무에서 네티사용하다 버퍼 사이즈초과시 oom:directBuffer 어쩌고로 에러를 뱉기때문에 요땐 쉽게 파악가능하긴함
- 하지만 그외의 다른 사유로 dm 오버플로우가난다면 찾기 어려울수도있겠다
- oom 이후 힙덤프상에 ㅜㄴ제가없다면 간접적으로 dm문제로 유추해야할듯
