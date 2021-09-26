---


---

<h2 id="스터디-일지">스터디 일지</h2>
<p>1주차 : 발표자 Albireo3754 (2021.08.16~2021.08.22)</p>
<ul>
<li>발표자료: <a href="https://albi-tech.tistory.com/5"></a><a href="https://albi-tech.tistory.com/5">https://albi-tech.tistory.com/5</a></li>
<li>과제 코드: <a href="https://albi-tech.tistory.com/6"></a><a href="https://albi-tech.tistory.com/6">https://albi-tech.tistory.com/6</a></li>
</ul>
<p>2주차 : 3챕터 발표자 jinia91(나)<br>
(2021.08.22~2021.08.29)</p>
<ul>
<li>발표자료 / 과제코드 : 본 지면으로 사용</li>
</ul>
<p>2주차 : 4챕터 발표자 자스어린이<br>
(2021.08.22~2021.08.29)</p>
<ul>
<li><a href="https://material-hurricane-4fa.notion.site/7a82c47919d142feb2af24ba2e7c78e3">발표자료 링크</a></li>
</ul>
<p>3주차 : 5챕터 발표자 캐프붕<br>
(2021.08.29~2021.09.05)</p>
<ul>
<li>발표자료 미기입</li>
</ul>
<p>3주차 : 6챕터 발표자 신입전향<br>
(2021.08.29~2021.09.05)</p>
<ul>
<li>발표자료 미기입</li>
</ul>
<h2 id="section"></h2>
<p><img src="https://user-images.githubusercontent.com/85499582/130334275-c14f1ae5-3953-4f29-8274-447b8e7df7bf.gif" alt="calculatorver_0 1"></p>
<h2 id="스터디-과제-계산기-만들기">0. 스터디 과제 계산기 만들기</h2>
<h3 id="주차--러프하게-기능만-구현하기">1주차 : 러프하게 기능만 구현하기</h3>
<h4 id="현재-코드의-문제점">현재 코드의 문제점</h4>
<ol>
<li>
<p>기능구현을 최우선으로 한만큼 절차적으로 코드를 작성하였으며 하나의 클래스에 모든 기능이 들어가 있음</p>
</li>
<li>
<p>메인 로직이라고 할 수 있는 사칙연산과 초기화, 등호연산(=)에 대한 분리가 안 이루어져있고 하나의 메소드에서 모두 수행하여 협업시 코드 리딩과 변경이 매우 힘들것으로 예상됨.</p>
</li>
<li>
<p>메소드 분리를 하지않아 코드의 중복이 다수 발생</p>
</li>
<li>
<p>위와같은 이유로 기능 확장시에도 많은 코드 수정이 따를것으로 예상됨.</p>
</li>
</ol>
<h4 id="추후-개선사항">추후 개선사항</h4>
<ul>
<li>
<p>단일책임원칙을 생각하여 역할과 책임을 객체에게 적절히 분배하고 시스템을 분할하여 재설계하기</p>
</li>
<li>
<p>사칙연산과 같은 로직들은 if-else if방식이 아닌 전략패턴을 적용하여 캡슐화하고 추상화를 통해 기능확장의 가능성을 열어두도록 설계해보기</p>
</li>
</ul>
<h3 id="주차-책임-주도-설계와-mvc패턴">2주차: 책임-주도 설계와 MVC패턴</h3>
<p>1주차에 계산기의 코드를 잠깐 살펴보면</p>
<p>Application)</p>
<pre><code>public class Application {  
   public static void main(String[] args) {  
      Calculator calculator = new Calculator();  
   }  
}
</code></pre>
<p>Calculator)</p>
<pre><code>class Calculator extends JFrame implements ActionListener {  
  ...................................중략
  xtField(30);  
  display.setText("");  

  Font bigFont = display.getFont().deriveFont(Font.PLAIN, 25f);  
  display.setFont(bigFont);      
  }  
  add(display, BorderLayout.NORTH);  
  add(panel, BorderLayout.CENTER);  
  setVisible(true);  
  pack();  
  
   }  
 .....................................중략
   public void actionPerformed(ActionEvent button) {  


  if (button.getActionCommand().equals("C")) {  

     display.setText("");  
     result = 0;  
     firstFlag = true;  
     return;  
  }  
  .......................................중략
</code></pre>
<p>사용자의 구동 메시지를 수신하고 행동하는 Application과<br>
구동과 계산 모두를 담당하는 Calculator</p>
<p>단 두개의 객체만으로 이루어져 절차적 설계로 만들어진 앱이지, 전혀 객체지향적이지 않은 모습을 보여준다.</p>
<p>만약 위의 코드를 누군가가 인수인계하여 수정하고 기능을 확장하거나, 유지보수해야한다고 상상해보자.</p>
<p>인수자는 코드의전체 문맥을 파악하기위해 몇번을 읽고 이해하기위해 노력해야할것이다.</p>
<p>그럼 이제부터 책임주도 설계와 MVC 패턴의 적용을 통해 객체지향의 시각으로 위의 코드를 리팩토링해보겠다.</p>
<h4 id="시스템의-책임-이해하고-쪼개기---책임주도-설계">시스템의 책임 이해하고 쪼개기 - 책임주도 설계</h4>
<p><strong>책임-주도 설계</strong>란 사용자의 메시지에 대한 시스템의 책임을 명확히 파악하고, 이 책임을 잘게 분할해가며 적절한 객체 혹은 역할에게 할당해나가는 <strong>분할정복과 비슷한</strong> 설계 방식이다.</p>
<p>계산기 애플리케이션을 책임 주소 설계로 바라보면 시스템의 메인 행동(책임)은 사용자의 계산 요청에 대한 적절한 응답이다. 이를 다시 분할해보면</p>
<ol>
<li>사용자의 프로그램 구동 요청에 대한 책임</li>
<li>사용자의 Input 을 받을 책임</li>
<li>Input값을 적절한 계산객체(서비스로직)에게 전달할 책임</li>
<li>계산할(서비스로직을 수행할) 책임</li>
<li>계산된 Output을 사용자에게 전달할 책임</li>
</ol>
<p>정도로 크게 5가지로 나눠볼 수 있다.</p>
<p>여기서 보다 원할한 설계를 위해 어느정도 친숙한 패턴인 MVC 패턴을 적용해보자.</p>
<p>MVC패턴은 주로 웹 애플리케이션에 사용되는 패턴이므로 실제 실무에서 일반 앱에 적용하기에는 적절하지 않으나 구현의 편의와 공부목적으로 시행하였다.</p>
<p>MVC 패턴은 애플리케이션을 모델, 뷰, 컨트롤러 세가지 관점으로 나누어 설계하는 방식으로 간략하게 요약하면</p>
<p><strong>VIEW 	: 사용자가 보게될 결과물을 생성하는 역할<br>
MODEL : 데이터를 관할하는 역할<br>
CONTROLLER: 요청이 들어올때, 해당 요청을 수행할 비지니스 로직을 제어하고, 흐름을 제어하는 역할</strong></p>
<p>로 구분된다.</p>
<p>여기서 비지니스 로직은 사람에 따라 model영역에 혹은 controller 영역에 두기도 하고 따로 SERVICE 영역으로 구분짓기도 한다.</p>
<p>위의 책임주도 설계를 통해 분할한 5개의 책임을 MVC 패턴에 맞춰</p>
<p>책임을 분할해 개발해야될 객체들을 다음 그림과 같이 판단해 보았다.</p>
<p><img src="https://github.com/jinia91/ReadingGroupStudy/blob/master/src/Untitled%20Diagram.jpg?raw=true" alt="enter image description here"></p>
<ol>
<li><a href="https://github.com/jinia91/ReadingGroupStudy/blob/master/src/main/Application.java">유저의 구동 메시지호출을 받는 객체/Application</a></li>
<li><a href="https://github.com/jinia91/ReadingGroupStudy/blob/master/src/main/Calculator.java">화면을 렌더링하고, I/O 책임을 담당하는 객체/Calculator</a></li>
<li><a href="https://github.com/jinia91/ReadingGroupStudy/blob/master/src/Controller/FrontController.java">클라이언트의 요청을 받아 서비스로직의 흐름을 제어하는 객체/FrontController</a></li>
<li><a href="https://github.com/jinia91/ReadingGroupStudy/tree/master/src/service">계산 로직들</a></li>
<li><a href="https://github.com/jinia91/ReadingGroupStudy/tree/master/src/dao">계산 로직에 필요한 메모리형 객체 DAO/MemoryResultStore</a></li>
<li><a href="https://github.com/jinia91/ReadingGroupStudy/blob/master/src/model/CalDto.java">데이터의 운반과 변경, 호출을 담당하는 객체/DTO</a></li>
</ol>
<h3 id="차후-개선사항">차후 개선사항</h3>
<p><img src="https://github.com/jinia91/ReadingGroupStudy/blob/master/src/Untitled%20Diagram2.jpg?raw=true" alt="enter image description here"></p>
<ul>
<li>전략패턴에 대한 이해도가 부족해서 공부 후 구현해보기</li>
<li>어댑터패턴 적용여부 판단</li>
<li>프론트 컨트롤러의 책임이 과한것 아닌가? 매퍼가 필요한지 판단</li>
<li>의존성 주입에 대해 공부하고 구현해보기</li>
</ul>
<h2 id="협력하는-객체들의-공동체">1. 협력하는 객체들의 공동체</h2>
<h3 id="객체지향이란">객체지향이란</h3>
<p>객체 지향이란, 애플리케이션을 <strong>1)상호작용하는 2)자율적인 객체들의 집합</strong>으로 보고, 객체를 이용해 <strong>3)시스템을 분할</strong>하는 방법론을 의미한다.</p>
<ul>
<li>
<p>1)객체들의 상호작용은 <strong>요청과 응답</strong>으로 구성되며, 요청은 추상화된 메시지를 통해서 전달되고 응답은 구체화된 메소드를 통해서 행해진다.</p>
</li>
<li>
<p>2)자율적인 객체란 <strong>상태</strong>와 <strong>행위</strong>를 가지며, 스스로 자기 자신을 책임지는 객체를 의미한다.</p>
</li>
<li>
<p>3)커다란 시스템의 행위를 구현하기 위해 내부의 객체들은 요청과 응답을 상호작용하는데 이를 <strong>협력</strong>으로 정의할 수 있다.</p>
</li>
<li>
<p>4)각 객체는 협력속에서 정해진 <strong>역할</strong>과 역할에 해당하는 <strong>책임</strong>이 존재한다.</p>
</li>
</ul>
<h2 id="이상한-나라의-객체">2. 이상한 나라의 객체</h2>
<p>객체란 <strong>상태</strong>와 <strong>행동</strong>을 가지며 <strong>식별가능한</strong> 개체(Entity) 혹은 사물(Object)이다.</p>
<p>객체의 상태는 변경가능하며(mutable) 변경시키는 것은 오로지  <strong>자신의  행동</strong>이여야하고(캡슐화), 외부에서는 자신의 상태를 접근할 수 없다. -&gt; <em>자율적인 객체</em><br>
이는 행동의 결과가 상태에 <strong>의존적</strong>이다라고 표현할 수 있다.</p>
<blockquote>
<p>프로그래밍에서 <strong>의존</strong>이란 의존하는 대상을 <strong>알고</strong>있음을 의미</p>
</blockquote>
<p>또한 행동은 행동 내에서 협력하는 다른 객체에 대해 메세지를 전송하기도 한다.</p>
<p>프로그래밍에서 객체를 구분하는데는 <strong>동등성(equality)</strong> 과 <strong>동일성(identical)</strong> 두가지 기준을 사용한다.</p>
<p><strong>동등성</strong>이란 값(value)가 같은지 다른지의 여부를 통해 객체의 일치 여부를 판단하는 기준이다.</p>
<blockquote>
<p>자바에서 String 클래스의 equals()메소드가 동등성의 원리로 재정의한 대표적인 예시.<br>
클래스를 만들때 객체의 동등성을 표현하고 싶다면 equals()메소드를 오버라이딩하여 값을 비교하면 된다.</p>
</blockquote>
<p><strong>동일성</strong>이란 객체가 완전히 일치하는지의 여부로, 객체는 식별자를 통해 동일성을 판단할 수 있다.</p>
<blockquote>
<p>자바에서 == 은 객체의 참조주소값을 비교하게 되는데 이를 통해 참조변수가 지목하는 객체가 동일한지 여부를 확인가능하다.</p>
</blockquote>
<h3 id="객체지향의-오해">객체지향의 오해</h3>
<p>객체지향은 현실의 <strong>모방</strong>이 아니라 <strong>은유</strong>이다.</p>
<p>객체지향 세계에서 은유된 개체 혹은 사물들은 의인화되어 다른 개체 혹은 사물에게 메세지를 전송하며 요청하고</p>
<p>메세지를 수신하고 이에 응답해 행동하며 그 행동은 자율적으로 개체 혹은 사물 자신의 상태를 변화시키고 다시 다른 개체 혹은 사물에게 메세지를 전송한다.</p>
<p>응답과 요청, 메시지의 수신과 송신, 행동과 상태변화의 무수한 반복을 통해 하나의 큰 협력을 이루고 협력은 시스템이 되어 우리가 만드는 앱이된다.</p>
<p>객체 지향의 설계는 이러한 의인화된 시스템을 창조하는 과정이다.</p>
<h2 id="타입과-추상화">3. 타입과 추상화</h2>
<p>객체지향의 시각에서 의인화된 시스템을 바라볼 때 구동중인 애플리케이션은</p>
<p>수많은 <strong>객체들이</strong> 바쁘게 <strong>행동</strong>하고 있는 <strong>협력</strong>활동, 혹은 협력하는 세상으로 볼 수 있다.</p>
<p>개발자로서 위와 같은 세상을 코드로 구현하려한다고 상상해보자.</p>
<p>모든 객체들을 손수 코드로 작성하려면 너무나 많은 코드가 필요하고 중복되는 코드도 많아 비효율적일 것이다.</p>
<p>이를 극복하기 위해 우리는 추상화라는 도구를 사용할 수 있다.</p>
<blockquote>
<p>객체지향에서 추상화란 의도를 가지고 목적을 정한뒤, 목적에 불필요한 부분을 제거하여 단순화하는것으로 정의할 수 있다.</p>
</blockquote>
<p>구체적인 방법으로 살펴보면 개별적인 객체들을 특정 목적을 가지고 그에 부합한 공통점을 추출해낸 뒤, 불필요한 부분을 덜어내어</p>
<p><strong>특정 목적에 해당하는 공통점</strong>을 가진 객체들의 집합, 묶음을 만들어낼 수 있다는 것이다.</p>
<p>여기서 <strong>특정 목적에 해당하는 공통점</strong>을 쉽게 말해 컨셉(Concept), 개념으로 축약할 수 있다.</p>
<p>즉, 하나의 <strong>컨셉(개념) 안에 속하는 객체들을 선별</strong>해 낼 수 있다면, 위에서 살펴본 객체들의 세상을 훨씬 단순하게 바라볼 수 있게되고 보다 쉽게 개발할 수 있을 것이다.</p>
<h3 id="타입type">타입(Type)</h3>
<p>객체지향에서는 이 컨셉이라는 단어를 보다 다듬어 <strong>타입(Type)</strong> 으로 부른다. 자바에서 항상 사용하는 데이터 타입(int, char…)이나 참조타입(String, Math, 그리고 우리가 정의한 클래스들)이 바로 여기에 해당하는 것이다.</p>
<p>그렇다면 우리는 객체들을 어떻게 타입으로 분류해야할까?</p>
<p>객체의 상태는 행동에 의해 변화될 수 있으므로 상태를 통해 타입을 분류하는것은 적절하지 못하며</p>
<p>객체들의 <strong>공통된 행동</strong>을 중심으로 타입으로 분류하는것이 적절하다.</p>
<p>객체를 공통된 행동으로 한데 묶고, 시간에 따른 <strong>상태 변화</strong>를 덜어냄으로서 추상화를 하여 분류하면</p>
<p>여러 객체들은 특정 행동을 하는 하나의 추상적 타입(컨셉)으로 분류화될것이고</p>
<p>이를 통해 어플리케이션의 세계를 보다 간략하게 파악하고 손쉽게 다룰 수 있게되는 것이다.</p>
<blockquote>
<p>자바에서는 개별 객체들을 추상화를 통한 개념으로 묶어 Class로 표현하고, 상위 계층의 타입은 부모 클래스 혹은 인터페이스로 표현할 수 있다. 즉 추상화(일반화)/특수화를 통해 상속이라는 방법론이 발명된것이다.</p>
</blockquote>
<h2 id="역할-책임-협력">4. 역할, 책임, 협력</h2>
<p>객체 지향의 시각에서 가장 중요한 것은 <strong>객체의 행동</strong>이다.<br>
하지만 객체는 스스로 행동을 시작하지 않으며 <strong>다른 객체의 요청</strong>과 <strong>그에 대한 응답으로</strong> 행동이 이루어 진다.</p>
<p>즉 객체는 혼자서 고립된 섬이 아니라 여러 객체들이 서로 <strong>상호작용</strong>하는 <strong>협력체, 협력 시스템</strong>인 것이다.</p>
<blockquote>
<p>협력 : 요청과 응답을 통한 객체들간의 상호작용</p>
</blockquote>
<p>그리고 어떤 객체가 요청(메시지)을 하면 그 요청을 들은(메시지를 받은, 메시지 호출을 받은) 객체는 <strong>응답(행동)해야할 책임</strong>이 있다.</p>
<p>여기서 객체는 <strong>여러가지</strong> (행동해야할)책임집합을 갖기도 하는데 이 책임은 반드시 응집도 있는 행위들의 집합이여야한다.</p>
<blockquote>
<p>여러 책임들이 응집도있다면 이는 <strong>하나의 큰 책임 집합</strong>으로 여겨질 수 있다</p>
</blockquote>
<p>만약 하나의 객체가 지나치게 많은 책임이나, 응집도가 떨어지는 책임집합을 갖고있다면</p>
<p>이는 너무 많은 책임을 갖고 있다는 것이며(SRP 위배), 객체지향설계가 적절하게 이루어 지지 않았다는 의미다.</p>
<blockquote>
<p>책임 : 메시지를 받은 객체가 응답해야 할 의무</p>
</blockquote>
<p>마지막으로, 역할을 이해하기에 앞서 3챕터의 내용을 잠깐 되새겨보자.</p>
<p>3챕터에서는 객체들의 공통된 행동을 묶어 추상화를 통해 타입으로 분류할 수 있다고 했다.</p>
<p>그런데 행동은 메시지에 대한 응답할 의무(책임)의 발현이다. 따라서 하나의 메시지에 대한 여러 객체들의 동일한 행동이 가능하다면, 이 객체들은 하나의 **역할(Role)**을 수행한다고도 말할 수 있을것이다.</p>
<blockquote>
<p>객체지향에서 역할이란 <strong>메세지를 수신하고 이를 책임질수 있는</strong>(행동할 수 있는) 능력을 의미한다.</p>
</blockquote>
<p>즉 역할이 가능한 객체들은 하나의 분류로 추상화될 수 있고 이를 방법론적으로 자바에서는 클래스/인터페이스로 구현할 수 있다.</p>
<h3 id="책임주도-설계">책임주도 설계</h3>
<p>2주차 계산기 과제에서 설명</p>
<h2 id="책임과-메세지">5. 책임과 메세지</h2>
<p>지난 4장까지 저자의 말을 간략하게 요약하면, 객체지향 관점에서 가장 중요한 것은 객체의 <strong>행동</strong>이며, 행동을 유발하는 것은 다른 객체가 보낸 <strong>메시지</strong>와 메시지에 대해 응답할 <strong>책임</strong>이다. 따라서 적절한 <strong>책임</strong>을 객체에게 할당하는 것이 설계에서 가장 중요한 것이라고 할 수 있다.</p>
<p>그렇다면 적절한 책임은 대체 무엇일까?</p>
<h3 id="자율적인-책임">자율적인 책임</h3>
<p>좋은 객체지향 설계를 위한 SOLID 원칙과 결합도를 생각해보면, 객체의 책임은 너무 커선 안되고, 객체간의 결합은 최대한 느슨해야한다고 한다. 즉 객체들은 서로간에 구속을 최소화하여 스스로가 최대한 자유롭게 판단할수 있을때, 유연한 설계가 이루어지는 것이다.</p>
<p>그렇다면 자유로운 객체가 되기 위해서는 할당된 책임이 자율적이여야 될 것이다.</p>
<p>이를 보다 구체화해보면, 자율적인 책임은 추상적인 메시지를 통해 주어지게 될 것이다.</p>
<p>만약 선생이란 객체가 학생이란 객체에게 학생이 오늘 공부한것을 알고 싶어서,</p>
<blockquote>
<p>“오늘 1교시에 필기한 노트랑 2교시에 필기한노트, 3교시에 필기한노트, 4교시에 필기한노트를 가져와”</p>
</blockquote>
<p>라고 메시지를 보낸다면, 학생객체는 그 4가지 노트를 반환하는수밖에없다.</p>
<p>즉 매개변수로 1교시공부량,2교시공부량,3교시공부량,4교시 공부량을 모두 입력받아 그만큼 구체적인 반환값을 요구한 메시지(메소드 호출)이며,</p>
<p>학생 객체는 이에대해 딱 정해진 반환값만 반환할 수 있을것이다.</p>
<p>애플리케이션에서 위와같은 설계를할 경우, 만약 기획자가 바뀌어 선생객체나 학생객체를 바꿀일이 생긴다면?</p>
<p>바뀐 학생객체는 공부를 5교시부터 열심히한다던가하는 등 다른 특성이있다면?</p>
<p>그럼 <strong>메시지를 다시 수정</strong>(메소드를 다시 수정)해야할일이 생기며 이는 유연성이 떨어지는 설계가 된다.</p>
<p>하지만 만약 처음부터 메시지가</p>
<blockquote>
<p>“오늘공부한거 가져와”</p>
</blockquote>
<p>라고 적당히 추상화되었다면, 선생과 학생이 아무리 바뀌어도 학생은 메시지의 책임에 스스로 행동을 결정할수 있게된다.</p>
<p>이처럼 <strong>적절히 추상화된 메시지</strong>가 <strong>적절한 책임</strong>을 부여하기 위한 핵심이다.</p>
<h3 id="다형성">다형성</h3>
<p>객체가 스스로 행동을 결정하는 것은 객체지향에서 다형성으로 구현된다.</p>
<p>위의 예시처럼 책임을 수행할 역할이 있는 객체들은 구체적인 메소드를 통해 행동할 수 있으며, 학생이라는 역할은 추상화된 메시지 덕분에 다른 학생, 심지어 학생이 아닌 다른 타입의 객체들로도 얼마든지 대체할 수 있게됬다.</p>
<p>메시지 송신자와 수신자간의 낮은 결합도가 생긴것이며, 이는 유연하고 확장 가능하고 재사용성이 높은 설계가 됨을 의미한다.</p>
<p>그리고 이 모든 결과는 <strong>적절하게 추상화된 메시지</strong>에서부터 시작한다.</p>
<h3 id="메시지와-인터페이스">메시지와 인터페이스</h3>
<p>추상화된 메시지를 수신할 수 있는 여러 개체들은 타입으로 추상화될 수 있고, 이를 보다 추상화시키면 상위클래스 또는 인터페이스라는 방식으로 구현될 수 있다.</p>
<p>즉 인터페이스를 정의하는 것은 메시지이며, 인터페이스는 수신할 수 있는 메시지 목록이라고 볼 수 있다.</p>
<blockquote>
<p>특정 개체가 인터페이스를 구현했다면 이 개체는 해당 메시지들을 수신할수 있는 역할이라는 의미</p>
</blockquote>
<p>여기서 중요한 사실은 인터페이스라는 개념을 작은 단위에도 적용가능하단 점이다.</p>
<p>즉 현재 설계시점에서 해당 역할을 수행하는 객체가 하나만 존재할 지라도, <strong>역할</strong>이 존재하는 이상, 하나의 객체도 역할에 해당하는 인터페이스와 그 인터페이스의 구현으로 쪼개서 생각할 수 있다.</p>
<p><img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&amp;fname=https://t1.daumcdn.net/cfile/tistory/99396B4B5C6CA36E01" alt="enter image description here"></p>
<blockquote>
<p>Service interface 와 service impl 관계처럼 모든 역할은 메시지를 수신할 껍데기인 인터페이스와 메시지의 책임을 수행할 구현체로 분리가능하다! 이때 컨트롤러는 서비스 인터페이스를 바라보며, SOLID 원칙에서 의존의 역전 원칙(DIP)을 준수하게된다. 이를 구현체를 캡슐화한다고 표현하기도한다.</p>
</blockquote>
<h2 id="객체-지도">6. 객체 지도</h2>
<p>소프트웨어 분야에서 예외가 없는 유일한 규칙은 요구사항이 항상 변경된다는 것이다. 변경에 발맞춰 빠르게 요구사항을 충족시키기 위해서는 좋은 설계가 뒷받침 되야 하고, 좋은 설계는 좋은 구조를 통해 이루어 진다.</p>
<p>객체지향에서 설계를 할때 가장 우선시되는것은 안정적인 객체 구조를 만들고 그 구조하에서 시스템 기능을 책임으로 나누어 객체에 분배하는 방식이다. 따라서 객체지향 설계를 제대로 해내기 위해서는 객체지향 설계의 대표적인 구조(모델)들을 알아보고 이해할 필요가 있다.</p>
<h3 id="도메인-모델--도메인-주도-설계ddd">도메인 모델 / 도메인 주도 설계(DDD)</h3>
<p>도메인 모델이란 사용자가 프로그램을 통해 <strong>이용하고자하는 분야/ 해결하고자 하는 영역(도메인)</strong> 을  추상화, 구조화해놓은 형태를 의미한다.<br>
예를 들어 은행업무 애플리케이션은 은행 업무를 이용하고자하는 클라이언트들이 사용하고, 은행업무를 수행하고자 하는 서버들이 구동할 것이다.</p>
<p>이때 <strong>은행 업무</strong> 라는 개념을 중심으로 애플리케이션을 구조화하는 것을 도메인 모델이라고 말한다.</p>
<p>도메인 모델을 사용함으로서 애플리케이션의 실사용자들도 개발되고 있는 앱의 구조와 흐름을 쉽게 파악하게 되고,</p>
<p>이를 바탕으로 이해관계자들의 요구사항과 개발자들의 구현간 일치율을 높여 변경사항을 줄이고 보다 요구사항에 적합한 개발을 빠르게 해낼수 있게 된다.</p>
<p><img src="https://mblogthumb-phinf.pstatic.net/MjAyMDA1MDdfMTMw/MDAxNTg4ODM2NTcwODUy.MjPDpg5CRWuDPjiXEb3iX2u9bCARNF3YCQDu8ABoE3Ag.Hcqx_FY76_8uzPfWonWdpxFrwvmzEPBWvsR8Wnu8TZsg.PNG.bernardokang/image.png?type=w800" alt="도메인 모델 예시"></p>
<h3 id="유스케이스">유스케이스</h3>
<p>도메인 모델이 클라이언트의 <strong>사용 영역</strong>을 중심으로 애플리케이션을 구조화해봤다면,</p>
<p>유스케이스 모델은 사용자가 애플리케이션을 <strong>실제 사용하는 시나리오</strong>에 초점을 맞추어 사용자 목표를 표현하는 방식이다.</p>
<p>다만 유스케이스 모델에서는 단지 사용자가 바라보는 시스템의 외부 관점만을 표현하며 내부의 설계에 대한 정보는 담지 않는다. 단지 시나리오의 집합일 뿐이며 설계 기법도 객체지향 기법도 아니므로</p>
<p>유스케이스에 집착하여 객체지향을 구현하는 접근법은 옳지 못하다.</p>
<h3 id="모든-도구를-활용하여-설계하기">모든 도구를 활용하여 설계하기</h3>
<p>애플리케이션을 만드는데 있어서 가장먼저 애플리케이션의 실사용 분야를 파악하고 이를 토대로 안정적인 구조를 만들기 위한 <strong>도메인 모델</strong></p>
<p>그리고 애플리케이션이 실제로 어떤 방식으로 클라이언트와 소통하고 어떤 기능이 필요한지를 서술하는 <strong>유스 케이스</strong></p>
<p>위의 두가지를 바탕으로 유스케이스에 기술된 기능들의 책임을 분할하여 적절한 객체를 찾아 할당하는 <strong>책임 주도 설계</strong></p>
<p>책의 저자는 위의 세가지를 중심으로 객체지향 설계방법을  다음과 같이 기술하고있다.</p>
<ul>
<li>요구사항을 식별하고 도출하는데 유스케이스를 사용하기</li>
<li>거대한 책임을 가진 시스템을 분할하여 객체에게 할당할때, 할당할 객체는 도메인모델에서 찾을것</li>
<li>객체의 이름은 도메인 모델에 포함된 개념부터 차용</li>
<li>책임은 도메인 모델에 정의한 개념에 부합하도록 할당</li>
<li>안정적인 도메인 모델을 기반으로 시스템 기능을 구현하며 도메인모델과 코드를 밀접하게 연관시키도록 노력하라</li>
</ul>
<h2 id="함께모으기">7. 함께모으기</h2>
<p>마틴 파울러는 소프트웨어의 객체지향 설계가 크게 세가지 관점에서 진행된다고 말했다.</p>
<p><strong>개념관점</strong> : 설계는 도메인 안에 존재하는 개념과 개념들 사이의 관계로 표현</p>
<p><strong>명세관점</strong> : 도메인영역을 벗어나 실제 객체들의 책임에 초점을 맞추고 객체의 인터페이스에 책임 부여를 설계</p>
<p><strong>구현관점</strong> 인터페이스를 구현한 객체가 실제로 어떻게 책임을 수행할것인지를 설계하는 관점으로 속성과 메서드 작성이 핵심</p>
<p>위의 과정은 순서대로가 아니라 어디까지나 관점의 영역이며 세가지 관점이 (자바의 경우) 클래스 안에서 잘 드러났을때 좋은 설계라 할 수 있을 것이다.</p>
<p>이제 책에서 나온 예시를 가지고 위의 관점을 적용하여 설계해보자</p>
<h3 id="커피-전문점-도메인도메인-분석-설계">커피 전문점 도메인(도메인 분석, 설계)</h3>
<ol>
<li>도메인 분석</li>
</ol>
<ul>
<li>
<p>커피 전문점의 핵심 비지니스 로직은 커피 판매이다. 따라서 커피 판매에 필요한 요구사항을 검토해보고 해당 요구사항에 필요한 객체들을 추려보자.</p>
</li>
<li>
<p>커피 메뉴는 총 4가지</p>
<ul>
<li>(아메리카노 1500원</li>
<li>카푸치노 2000원</li>
<li>카라멜 마키아또 2500원</li>
<li>에스프레소 2500원</li>
</ul>
</li>
<li>
<p>판매 비지니스 로직( <strong>유즈 케이스</strong> )</p>
<ul>
<li>손님은 커피메뉴에서 커피를 고를수 있고</li>
<li>고른 커피를 바리스타에게 제출하면</li>
<li>바리스타는 제출된 커피를 제조해서 손님에게 전달</li>
</ul>
</li>
<li>
<p>이제 커피 전문점에서 객체가 될 수 있는 후보들을 최대한 추려보자.<br>
우선 <strong>1. 손님들</strong>이 있을 것이고 <strong>2. 커피</strong> 와  <strong>3. 커피를 파는 사람</strong>이 존재할 것이다. 그리고 커피 구매 정보전달을 위한 <strong>4. 메뉴판</strong>과 <strong>5. 메뉴들</strong>을 생각해 볼 수 있다.</p>
</li>
<li>
<p>여기서 추가로 실무단계라면 여러 주문들을 별도로 다루기 위해 <strong>주문객체</strong>를 추가로 생각해 볼 수도 있다. 예제는 편의를 위해 일회성의 주문만을 고려하자</p>
</li>
<li>
<p>위의 객체 후보들을 추상화하여 클래스단위(타입)로 다뤄보면</p>
<ul>
<li>Customer</li>
<li>Barista</li>
<li>TotalMenu</li>
<li>CoffeeMenu</li>
<li>Coffee<br>
다음과 같이 추상화해볼 수 있을것이다.<br>
여기서 CoffeeMenu는 TotalMenu에 포함된 <strong>합성관계</strong> 또는 <strong>포함관계</strong> 이며, 이를 UML 다이어그램으로 도식화하면 아래와 같다.</li>
</ul>
</li>
</ul>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV8AAAEFCAYAAABEoOQQAAAAAXNSR0IArs4c6QAABeV0RVh0bXhmaWxlACUzQ214ZmlsZSUyMGhvc3QlM0QlMjJhcHAuZGlhZ3JhbXMubmV0JTIyJTIwbW9kaWZpZWQlM0QlMjIyMDIxLTA5LTI2VDAyJTNBMjklM0EwNi4zMzdaJTIyJTIwYWdlbnQlM0QlMjI1LjAlMjAoV2luZG93cyUyME5UJTIwMTAuMCUzQiUyMFdpbjY0JTNCJTIweDY0KSUyMEFwcGxlV2ViS2l0JTJGNTM3LjM2JTIwKEtIVE1MJTJDJTIwbGlrZSUyMEdlY2tvKSUyMENocm9tZSUyRjk0LjAuNDYwNi42MSUyMFNhZmFyaSUyRjUzNy4zNiUyMiUyMGV0YWclM0QlMjJXbzB6WmZ1QVBlYWI4b19BbGkyUSUyMiUyMHZlcnNpb24lM0QlMjIxNS4wLjYlMjIlMjB0eXBlJTNEJTIyZ29vZ2xlJTIyJTNFJTNDZGlhZ3JhbSUyMGlkJTNEJTIyUjJsRUVFVUJkRk1qTGxoSXJ4MDAlMjIlMjBuYW1lJTNEJTIyUGFnZS0xJTIyJTNFelZodGI1c3dFUDQxU051SFJZQkRtM3hNMG1TYnRFcFZNNm50UndzT3NHWXdNMDREJTJGZld6aXdrdlR0YWtTMGVxcU9LZU81JTJGTmM0JTJGdEV4WmFKTVZYanJQNGxnVkFMZGNPQ2d2ZFdLNTdQWEhsZndXVUZUQkdWeFVRY1JKVWtOTUFhJTJGSUNHclExdWlFQjVKMUF3UmdWSk91Q1BrdFQ4RVVIdzV5emJUY3NaTFE3YTRZak1JQzFqNm1KUHBCQXhCVTY4ZXdHJTJGd1lraXV1WkhWdDdFbHdIYXlDUGNjQzJIUWdLc1dLcDBFdThBNTdnRkZJaFBiZVklMkZ3SnVlY3RZQ1BXbU04dGR5ViUyQm9va2NSWXhFRm5KRjg1TE5Fd240dVExWWhUZ2hWTkxjU3pYVWlPUjFhV21qQkdSUFZVMUlzZ0twUzFXV28xclE2NE4zeHdGWGVJd2JjSjQ5MnRONCUyQnJGNlMzOSUyRm5zeCUyRkZoTk12T3NzenBodk43MDhtc0JwMkMlMkJubTB3SUxpQmd2UDJ2R1JGbVhnYk5OR29CS2JWdG92bzJKZ0hXR2ZlWGRTdDFKTEJZSmxaWWpIJTJGVWt3QVVVQjFmdjdEaVIwZ1dXZ09DbERORUQzR3RkSWkxYkIybDcyNGpBcWNzWXR3UndwVEdzaXhydFVqZGN5UWROMXduVXVRWjFDeGFHQUpxN3dSa2JUeSUyQk5NV1F5dHNtRlRNNEhKNnN2TDNkd3NzWUdXWFBNU1M3d3hYR0YzS0c1OGc1dXhhSDM0T1RTcUpvWVZCa2tRUnJNMUVVdHJaU2wwQ1ZGdmpndkh4V0JJNjgybjlxJTJCbTBLelcxbGxiUlZFdElaSjY2bmxhUVlwb3g2ajclMkJUQWFBaDY5TXZWc3czMzRlMmpSMkFlZ1hqclBqVEwyU3FYdDZkYU5jYUJZa0dldTh2ZFYwSTl3eDBqcjgyRlZndXllNGZRdUtlQzZqWDFxUFpWMzAlMkZrOVk3JTJCYVM5UnhZT1JTSllkbDYyd1RBWGtmMWt3NmkzWTZiUWc4cUhLMk1oMXglMkJuN0ZUd2RTTUhIcW5FdzlhQURaODNKNnVsWGRUciUyQkwlMkJwQnp2amoxZU9ZSGU5cDhybDRHZlRhdnQxWmNLb01qTHVybiUyQmlBRE01V0tiUEJmdTlHYjIlMkZ6MXE3JTJGeDQxJTJCeEhYaVhwSVNIRzg2OHM2amhUMnBQbG9OWm85bnFLRlYlMkIzMnRIYzZ6Nm9ORVNBclZBODd6R0dmS1QzSjJMejA0alZTbWVVZ29YVERLJTJCR3RXZVNtcnYlMkZQMGcyanE5bmcwJTJCMEdFUmdpWm91aWY1a2QwaE5Kc1BpOVVoV2clMkJDYUhsSHclM0QlM0QlM0MlMkZkaWFncmFtJTNFJTNDJTJGbXhmaWxlJTNFlzYmtQAAHXNJREFUeF7tnV2oVdd2x4flllYpTVMlBAQJ9kFJGwSxIaDCJWnRPKQBAxrQEwg+SFRsLabQev2+0hZtDKKCD1KoCppCSqAQfQkXVAghFeyTQpAQkJJUyQeiFNq7y1ieue88y73215xrzTHX+m0IJmevNeaY//+Yvz32XPPEecILBVAABVCgcQXmNT4iA6IACqAACgjwpQhQAAVQIIECwDeB6AyJAiiAAsCXGkABFECBBApUwbeXIBeGbFYBPnib1XvYaKw3O17UlclT660Svr0e9VCXC6njzptX2A58Uxvxm/F7rDc7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">
<p>이제 간단한 도메인 모델을 만들었고 여기에 커피 주문이라는 비지니스 로직상의 메시지 흐름들을 생각해보자</p>
<ol start="2">
<li>
<p>메시지와 책임</p>
<p>커피 주문에 필요한 메시지는 어떤것들이 있을까 순차적으로 생각해보면 다음과 같이 4가지 메시지로 축약해볼 수 있다.</p>
<ul>
<li>커피를 주문해라(String coffeeRequest)</li>
<li>메뉴항목에서 커피메뉴를 찾아라(String coffeeRequest)
<ul>
<li>CoffeeMenu 타입으로 반환</li>
</ul>
</li>
<li>커피를 주문해라(CoffeeMenu coffeeMenu)
<ul>
<li>Coffee 타입으로 반환</li>
</ul>
</li>
<li>커피를 만들어라(CoffeeMenu coffeeMenu)
<ul>
<li>Coffee 타입으로 반환</li>
</ul>
</li>
</ul>
<p>이제 다음 메시지들을 객체에 할당해주면 아래와 같은 시퀸스 다이어그램(축약형)이 완성된다.<br>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkUAAAEPCAYAAABMVbBWAAAAAXNSR0IArs4c6QAACJ90RVh0bXhmaWxlACUzQ214ZmlsZSUyMGhvc3QlM0QlMjJhcHAuZGlhZ3JhbXMubmV0JTIyJTIwbW9kaWZpZWQlM0QlMjIyMDIxLTA5LTI2VDAyJTNBNTElM0EyMS40OTVaJTIyJTIwYWdlbnQlM0QlMjI1LjAlMjAoV2luZG93cyUyME5UJTIwMTAuMCUzQiUyMFdpbjY0JTNCJTIweDY0KSUyMEFwcGxlV2ViS2l0JTJGNTM3LjM2JTIwKEtIVE1MJTJDJTIwbGlrZSUyMEdlY2tvKSUyMENocm9tZSUyRjk0LjAuNDYwNi42MSUyMFNhZmFyaSUyRjUzNy4zNiUyMiUyMGV0YWclM0QlMjJERnhyYVZoR293VHZaZEN4MEdvdCUyMiUyMHZlcnNpb24lM0QlMjIxNS4wLjYlMjIlMjB0eXBlJTNEJTIyZ29vZ2xlJTIyJTNFJTNDZGlhZ3JhbSUyMGlkJTNEJTIyUjJsRUVFVUJkRk1qTGxoSXJ4MDAlMjIlMjBuYW1lJTNEJTIyUGFnZS0xJTIyJTNFN1ZwdGI2TTRFUDQxU0hzZk5nSnNTUGdZOHJKN1VpdFYyNU8yJTJCOUVGaCUyRmdXY05hWUp0bGZmemFZQk95a1NYdlpKSnU3cXFyczhUQ0daJTJCYVpHVnUxd0NoYmZXSm9NYiUyQm5NVTR0MTQ1WEZoaGJydHNmdU9LdkZLeHJBUVIlMkJMVWdZaVd1UnN4VThrcDlZQ1cwbExVbU1pNDRpcHpUbFpORVZSalRQY2NRN01zUVlYWGJWWmpUdDdycEFDVFlFanhGS1RlbFhFdk41TFIxNDlsYiUyQkdaTmszdXpzMkdvbFE0MnlFaFJ6Rk5ObFI0UlhmRXB6cmw3eEFiTU01VGpuWXVVZXNlJTJCWVdkNWt6cm44MHFIbFRzWHZUR3IzRWtxVEZLTUZLWG9SellRNEtvVEtkSVl5a2txWVc0WkNaVWhzQnlZV0dERktlVDNLVmlPY1NsYzFicWpmYWJwbmRZTURrM2FQZU9CTDltUW5qOHV2MDUlMkZaanolMkZENGQxcXdOS1B5c29MU2t1RjcxJTJCVUklMkZuWVBjN0xEeVBFY1VMWiUyQmclMkJGR0Y4M2JtQzB6R01zVGRzV0NKZHp3dkhqQWtWeWRTbmlUc2ptUEV2RnpCRkR0UWxtSEslMkYydnIyendVU0VMcVlaNW13dFZOUURibCUyQjVTSVd0QTlSOHVRMENwM0hqdkJVQXZwSWg1ZFJrWTNxTGxSZ291TjRBblFzTjdBeVVjQ3hpVjAwcDQzT2EwQnlsazYwMDdPSzQxYm1qZEtIUSUyQnh0enZsWkVSQ1dudTdDVkc3Mk9ySGd2V3JJSXYlMkZKRlFORVpzUVR6UTBGamVvcmhGSEh5MG4yUGs4TU8zUDhxN1BDaXNCdW9qOHFDQyUyQlBzNmxLRGUlMkZIVUFPMWJpMUY0Wkl4Nmw0eFJNeUdIaUpHQ282c0xVZUJlT2tROWs4OTBOc1A0NGxCNSUyRnJWQkZSeEI1andleXQ1V3pIS2E0eTRvNHNQWiUyQmtrQzJQT2E2YmYyMm5pbDBLMW5helU3bHI0bWxDMm92QjFJTmJLaldhbDJlS0NrNm9XVnB3RFk0Nm5HUkoxVjFGUHR6dlNBSVRlQVhVTjEyakVNQ2NqUnVxVzJrQXJGRzE3WWdWcHcxQmEzb2JMQjlGJTJCMGlXWXRHRWFjbW1WVEhFY1djbGhtYWEwQVFra2tJbzQlMkJkJTJCZ1pwdyUyQjBJSnpRWEtnOFV5NUtiMHRobUpKRUxuQ3FFWktXUENVNUhtME9Zekt3WmlSTlJ6U1ZXNGlOZ1YzOW5JYTlqbk80Rm9PemR1bm1DZWMxOWtZcEtnb1M3U0h3Ujd0bmc2RE5ZYnZuUTNpQXg5Vk1IQUdKJTJCQ0xNM2tqdUkyb3V1R1FTY0R6TjRmMTNKZ0hYMWd6cDJXUlBFamdaVDgxemhkTVRjMnN5c3NMUUdrSnJNclpFWWdwSFNqZ0VjandSUzBKaFVLMTZWZ2lsSkJoWGFuNHFzQTZmQmRYOVJJNCUyQlBISkc4c1NTbHlPeTFwcW5ha0U4M28yOWdqUDZIVGRzVmNXbFRXQWxRaW9EUkNKOE1OdVJHaklTeDFWYnVhdUVkNHY4S2ZLQUhoWndSeFczZDRTbDd2WFRKUUt6NDNGciUyRndvUEJ0S3pZakFJS2c5V3JoeU9xNldoWEpVeFlGdmhSQTdFMHVBdFh2NkNmNVM0NExmc2JLMWwyMUM1N1d6JTJGbk00R1p0RUZ2U3Ja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"></p>
</li>
<li>
<p>인터페이스 정리하기</p>
</li>
</ol>
<p>완성된 도메인 모델을 바탕으로 실제 애플리케이션상에서 메시지를 송수신할 인터페이스를 만들어보자</p>
<pre><code>package coffee;

public class InterfaceGruop {

	public interface Customer {
		public void order(String coffee);
	}

	public interface CoffeeMenu {
	}

	public interface TotalMenu {
		public CoffeeMenu choice(String coffee);
	}

	public interface Barista {
		public Coffee makeCoffee(CoffeeMenu coffeeMenu);
	}

	public interface Coffee{
	
	}
</code></pre>
<p>}</p>
<p>처음 설계한 대로 5가지 인터페이스가 완성되고 3가지 메세지 호출과 Coffee 생성자를 통해 나중에 구현할 커피 만들어라 메세지호출까지 총 4가지 메세지 호출이 완성될 수 있다.</p>
<ol start="4">
<li>구현하기</li>
</ol>
<p>이제 위의 인터페이스를 구현하는 실제 객체들을 작성하면 모든 개발이 끝난다!</p>
<p>손님 구현 클래스</p>
<pre><code>package coffee;

import coffee.InterfaceGruop.Barista;
import coffee.InterfaceGruop.Coffee;
import coffee.InterfaceGruop.CoffeeMenu;
import coffee.InterfaceGruop.Customer;
import coffee.InterfaceGruop.TotalMenu;

class CustomerImple implements Customer{

	@Override
	public void order(String coffee, TotalMenu totalMenu, Barista barista) {
	    CoffeeMenu coffeeMenu = totalMenu.choice(coffee);
	    Coffee cof = barista.makeCoffee(coffeeMenu);

	}
}
</code></pre>
<p>메뉴판 구현 클래스</p>
<pre><code>package coffee;
import java.util.List;
import coffee.InterfaceGruop.CoffeeMenu;
import coffee.InterfaceGruop.TotalMenu;

class TotalMenuImpl implements TotalMenu {

	private List&lt;CoffeeMenu&gt; coffeeMenuList;

	public TotalMenuImpl(List&lt;CoffeeMenu&gt; coffeeMenuList) {
	this.coffeeMenuList = coffeeMenuList;
}

	public CoffeeMenu choice(String coffee) {
		for (CoffeeMenu each : coffeeMenuList) {
			if (each.getName().equals(coffee)) {
				return each;
			}
		}
	return null;
	}
}	
</code></pre>
<p>세부 메뉴 구현 클래스</p>
<pre><code>package coffee;

import coffee.InterfaceGruop.CoffeeMenu;

public class CoffeeMenuImpl implements CoffeeMenu {

	private String name;
	private int price;

	public CoffeeMenuImpl(String name, int price) {
		this.name = name;
		this.price = price;
	}

	@Override
	public String getName() {
		return name;
	}
	@Override
	public int getPrice() {
		return price;
	}
}
</code></pre>
<p>커피 구현 클래스</p>
<pre><code>package coffee;

import coffee.InterfaceGruop.Coffee;
import coffee.InterfaceGruop.CoffeeMenu;

public class CoffeeImpl implements Coffee {

	private String name;
	private int price;

	public CoffeeImpl(CoffeeMenu coffeeMenu) {
		this.name = coffeeMenu.getName();
		this.price = coffeeMenu.getPrice();
	}
}
</code></pre>
<p>바리스타 구현 클래스</p>
<pre><code>package coffee;

import coffee.InterfaceGruop.Barista;
import coffee.InterfaceGruop.Coffee;
import coffee.InterfaceGruop.CoffeeMenu;

public class BaristaImpl implements Barista {

	@Override
	public Coffee makeCoffee(CoffeeMenu coffeeMenu) {
		Coffee coffee = new CoffeeImpl(coffeeMenu);
		return coffee;
	}
}
</code></pre>
<p>위와같이 구현된다. 여기서 인터페이스에 어느정도 수정이 있었는데</p>
<p>package coffee;</p>
<p>class InterfaceGruop {</p>
<pre><code>public interface Customer {
	public void order(String coffee,TotalMenu totalMenu, Barista barista);
}

public interface CoffeeMenu {
	public String getName();
	public int getPrice();
}

public interface TotalMenu {
	public CoffeeMenu choice(String coffee);
}

public interface Barista {
	public Coffee makeCoffee(CoffeeMenu coffeeMenu);
}

public interface Coffee{
	
}
</code></pre>
<p>}</p>
<p>손님 클래스의 객체가 주문하는 과정에서 바리스타와 메뉴판을 알아야함을 뒤늦게 파악하여 의존성을 주입해주기 위해 메시지에 인자를 추가하였다.</p>
<p>이처럼 최초의 설계는 구현과정에서 얼마든지 변경될 수 있으며, 최초의 설계는 어디까지나 대략적인 얼개에 불과하다는것을 잊지말자.</p>
<h3 id="※-인터페이스와-구현-분리는-언제나-중요함">※ 인터페이스와 구현 분리는 언제나 중요함!</h3>
<p>명세관점에서 객체의 인터페이스간 소통이 실제 훌륭한 설계를 결정하는것이다!</p>

