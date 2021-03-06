---


---

<h2 id="유스케이스-모델링">유스케이스 모델링</h2>
<h3 id="유스케이스-모델링이란">유스케이스 모델링이란?</h3>
<ul>
<li>기능 모델링의 한 종류로 이벤트 및 반응방식에효율적</li>
<li>사용자와 시스템간의 교류를 표현!</li>
<li>사용자 관점에서 시스템의 요구사항을 설계하는것</li>
<li>전 공정에서 사용 가능</li>
<li>시스템이 할일(USE CASE) 와 사용자(ACTOR) 로 구성</li>
</ul>
<h3 id="유스케이스-다이어그램">유스케이스 다이어그램</h3>
<p>동적(행위) 다이어그램으로 시스템내의활동들의 흐름을 보여줌</p>
<p>여러 업무 프로세스를 설명하는데 자주 활용</p>
<h4 id="구성요소">구성요소</h4>
<ul>
<li>
<p>ACTOR : 시스템과 상호작용하는 외부존재(사용자가될수도, 시스템이 될수도있음 다양함)</p>
</li>
<li>
<p>SYSTEM : 네모로 표현</p>
</li>
<li>
<p>USECASE : 시스템에서 제공하는 기능으로 동그라미로 표현</p>
</li>
</ul>
<p><img src="https://github.com/jinia91/blogTest/blob/main/img/UseCaseDiagram1.png?raw=true" alt="enter image description here"></p>
<h4 id="관계의-종류">관계의 종류</h4>
<ul>
<li>
<p>연관관계</p>
<ul>
<li>활성화 : actor -&gt; 유스케이스<br>
액터가 유스케이스를 활성화시킴</li>
<li>수행결과 통보 : 유스케이스 -&gt; actor<br>
유스케이스가  액터에게 통보 또는 외부 시스템에 서비스실행 요청</li>
</ul>
</li>
<li>
<p>포함관계(한 유스케이스가 다른 유스케이스 기능을 포함, 반드시 해야하는 관계!)&lt;&lt;include&gt;&gt;</p>
<ul>
<li>
<p>ex) 출퇴근 관리 기능 업무 기술서 유스케이스 작성시</p>
<ul>
<li>로그인 기능</li>
<li>출근시간 기록 기능</li>
<li>두개의 유스케이스는 로그인 -&gt; 출근시간기록 순서로 반드시 실행되므로 &lt;&lt;include&gt;&gt; 관계(포함관계)라고 말할수 있음</li>
</ul>
</li>
<li>
<p>표기법 : 출근시간 기록 --&lt;&lt;include&gt;&gt; --&gt; 로그인</p>
</li>
<li>
<p>포함유스케이스를 사용하는 이유는 유스케이스의 재사용목적, 필수라고 명시해놨으므로 다른 유스케이스에서 로그인 기능을 표시할때 포함관계 기능들이 실행될것임을 짐작할 수 있음</p>
</li>
</ul>
</li>
<li>
<p>확장관계(기본 유스케이스에서 특정 조건이나 액터의 선택에 따라 발생하는 유스케이스, 기능이 실행될수도 있다! 반드시는아님)&lt;&lt;extend&gt;&gt;</p>
<ul>
<li>
<p>ex) 게시판 등록 기능과 파일 업로드 기능</p>
</li>
<li>
<p>표기법 : 게시판 등록&lt;— &lt;&lt;extend&gt;&gt; ---- 파일 업로드<br>
포함관계랑은 방향이 다름! 주의!</p>
</li>
</ul>
</li>
<li>
<p>일반화 관계(상속관계라 보면 편함)</p>
<ul>
<li>ex) 게시물 검색 &lt;- 제목검색/내용검색<br>
추상화기능과 상세 기능</li>
</ul>
</li>
</ul>
<h4 id="유스케이스-다이어그램-작업-과정">유스케이스 다이어그램 작업 과정</h4>
<ol>
<li>액터 식별</li>
<li>유스케이스 식별(사용하려는 기능 도출)</li>
<li>도출한액터, 유스케이스 무작위 단순 배치</li>
<li>중복의미의 유스케이스 제거, 불필요한 유스케이스 제거, 그루핑</li>
<li>관계설정</li>
</ol>
<h3 id="커머스-쇼핑몰-유스케이스-실습">커머스 쇼핑몰 유스케이스 실습</h3>
<p><img src="https://github.com/jinia91/blogTest/blob/main/img/%EC%A4%91%EA%B3%A0%EB%82%98%EB%9D%BC.png?raw=true" alt="enter image description here"></p>
<h3 id="유스케이스-작성시-유의사항">유스케이스 작성시 유의사항</h3>
<ul>
<li>유스케이스간에는 실선연결 하면 안됨<br>
실선은 연관관계를 의미하며 연관관계는 액터와 유스케이스간에만 성립</li>
<li>유스케이스간의 관계가 지나치게 복잡할경우 합의를 통해 간략화도 가능(uml의 정답은 없고 어디까지나 의사소통 도구임을 인지하자)</li>
</ul>
<h3 id="실습-2">실습 2<img src="https://github.com/jinia91/blogTest/blob/main/img/%EC%87%BC%ED%95%91%EB%AA%B0.png?raw=true" alt="enter image description here"></h3>

