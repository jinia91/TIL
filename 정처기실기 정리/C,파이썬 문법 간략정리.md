---


---

<h2 id="변수-기초">변수 기초</h2>
<ul>
<li>문자열 :
<ul>
<li>C : char[]</li>
<li>C++ : string</li>
</ul>
</li>
<li>파이썬은 자료타입 x</li>
</ul>
<h2 id="c">C</h2>
<ul>
<li>
<h4 id="c-배열-선언">C 배열 선언</h4>
</li>
</ul>
<p>int a[5] = {1,2};<br>
// 공간이 5개인 a 배열 생성, 1,2,0,0,0 으로초기화됨</p>
<ul>
<li>
<h4 id="포인터-간략-요약">포인터 간략 요약</h4>
</li>
</ul>
<p>int a = 10;<br>
int* b = &amp;a;<br>
-&gt; 데이터타입에 포인터*가 붙어있으므로<br>
<strong>b라는 변수는 int 값을 가진 변수의 주소를 가리키는 포인터 변수</strong>라고 읽으면 됨<br>
이때 &amp;a는 a변수의 주소</p>
<ul>
<li>
<h4 id="입력">입력</h4>
</li>
<li>scanf(포맷, 변수명)<br>
scanf("%c %d", &amp;a, &amp;b);</li>
</ul>
<h2 id="c-1">C++</h2>
<ul>
<li>
<p>불린 : C++ bool</p>
</li>
<li>
<h4 id="단순출력">단순출력</h4>
<p>std::cout &lt;&lt; “문자열”<br>
using namespace std; 선언시<br>
cout&lt;&lt; “”; 가능</p>
</li>
<li>
<h4 id="개행">개행</h4>
<p>std::endl;<br>
cout &lt;&lt; “hello” &lt;&lt; endl &lt;&lt; “world”;</p>
<blockquote>
<p>hello<br>
world</p>
</blockquote>
</li>
<li>
<h4 id="입력-1">입력</h4>
<p>cin &gt;&gt; a &gt;&gt; b;<br>
cout &lt;&lt; a &lt;&lt; b</p>
</li>
<li>
<h4 id="virtual-키워드가-있어야지만-오버라이딩이-가능">virtual 키워드가 있어야지만 오버라이딩이 가능!</h4>
</li>
</ul>
<h2 id="파이썬">파이썬</h2>
<ul>
<li>
<h4 id="출력">출력</h4>
</li>
</ul>
<p>print(“문자열”) // 출력후 개행 파이썬은 기본이 개행이다<br>
print(“문자열”, end=’ ') // 출력후 개행을 하지 않음</p>
<ul>
<li>
<h4 id="입력-2">입력</h4>
s = input()<br>
s = eval(변수명)</li>
<li>
<h4 id="for-문">for 문</h4>
for  변수 in range (시작값, 끝값+1) : 명령문<br>
for 변수 in range (반복횟수) : 명령문
<blockquote>
<p>for i in range (1, 11) :<br>
sum = sum + i</p>
</blockquote>
</li>
</ul>
<h3 id="파이썬의-자료형">파이썬의 자료형</h3>
<ul>
<li>
<p>세트형(해쉬셋같은 개념)<br>
선언방법 : S = {1,5,7}<br>
S.add(3)<br>
print(S)<br>
// {1,3,5,7}<br>
S.add(5) // 중복이므로 의미x<br>
S.update([1,2,3,4]) // 1,2,3,4를 한번에 다 추가한다는 의미 중복거르고<br>
print(S)<br>
//{1,2,3,4,5,7}<br>
S.remove</p>
</li>
<li>
<p>리스트형(가변적으로 크기가 변하는 선형리스트 ArrayList)<br>
선언방법 : l=[3,5,7]<br>
l.append(3)<br>
print(l)<br>
// [3,5,7,3]<br>
l.insert(2,4) // 2번째자리에 4 삽입<br>
print(l)<br>
//[3,5,4,7,3]<br>
l.remove(3) // 앞에서부터 3발견하면 하나 삭제<br>
//[5,4,7,3]<br>
print(l[ : 2]) // 2까지 즉 0,1을 출력<br>
//[5,4]</p>
</li>
<li>
<p>딕셔너리형(맵 구조)<br>
선언방법 : d = {‘a’ : 5, ‘c’ : 7}<br>
d[‘K’] = 7<br>
// {‘a’ : 5, ‘c’ : 7,‘K’ : 7}<br>
del d[‘c’]<br>
// {‘a’ : 5,‘K’ : 7}</p>
</li>
<li>
<h4 id="파이썬에서-클래스와-함수-정의">파이썬에서 클래스와 함수 정의</h4>
<p>class 클래스명 :<br>
def 메서드명(self, 변수명, …) :<br>
명령어</p>
<blockquote>
<p>class A:<br>
def add(self, a,b) :<br>
sum = a+ b<br>
return sum</p>
</blockquote>
</li>
<li>
<h4 id="생성자">생성자</h4>
<p>def __init__(self,…)</p>
</li>
</ul>

