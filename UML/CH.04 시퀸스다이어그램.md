---


---

<h2 id="시퀸스-다이어그램">시퀸스 다이어그램</h2>
<ul>
<li>
<p>동적 다이어그램의 한종류로 시스템 내부에서 동작하는 객체들 사이의 주고 받는 메시지를 시간 순서를 강조하여 표현</p>
</li>
<li>
<p>생명선 : 액터, 객체, 컴포넌트의 인스턴스등 상호작용에 참여하는 구체적인 대상에 연결하여 시간을 표현하는 선으로 끊겨있으면 소멸됨을 의미함</p>
</li>
<li>
<p>메시지 : 객체간의 호출과 수신</p>
</li>
<li>
<p>활성화 막대 : 메시지를 수신받고 송신하며 객체가 활성화 되는 시점<br>
<img src="https://github.com/jinia91/blogTest/blob/main/%EC%8B%9C%ED%80%B8%EC%8A%A4%20%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.png?raw=true" alt="enter image description here"></p>
</li>
</ul>
<h3 id="메시지의-종류">메시지의 종류</h3>
<p><img src="https://github.com/jinia91/blogTest/blob/main/img/%EC%8B%9C%ED%80%B8%EC%8A%A4%20%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8%20%EB%A9%94%EC%8B%9C%EC%A7%80%EC%A2%85%EB%A5%98.png?raw=true" alt="enter image description here"></p>
<ol>
<li>비동기적 메시지 : 송신자를 대기시키지 않음(아작스통신)</li>
<li>동기적 메시지 : 송신자를 대기</li>
<li>대답 메시지 : 동기적 메시지의 수행 결과</li>
<li>생성 메시지 : 생명선 생성</li>
<li>발견 메시지 : 모르는 송신자로부터의 메시지</li>
<li>유실된 메시지 : 모르는 수신자로 메시지전송</li>
</ol>
<h3 id="대안-흐름">대안 흐름</h3>
<blockquote>
<p>실무에서 보통 시퀸스 다이어그램으론 통 기본흐름 / 액티비티 다이어그램으로 대안 흐름을 표현하는편</p>
</blockquote>
<p>일반적인 로직과 달리 특정 에러를 분기로 대안 상황을 시퀸스 다이어 그램으로 표현 가능<br>
- 결합조각<br>
- 상호작용 연산자<br>
- ALT : 대체(조건)<br>
- OPT : 옵션<br>
- LOOP : 반복<br>
- BREAK : 중단<br>
- 가드(메시지가 수행되는 조건)</p>
<h3 id="실습">실습</h3>
<p><img src="https://github.com/jinia91/blogTest/blob/main/t%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A41.%20%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.png?raw=true" alt="enter image description here"></p>

