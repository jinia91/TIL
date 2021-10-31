---


---

<h2 id="e-r-모델링">E-R 모델링</h2>
<p>개체 관계도, 요구사항 분석에서 얻어낸 엔티티와 속성들을 그림으로 그려내어 그 관계를 도출한 것</p>
<h3 id="주식별자">주식별자</h3>
<ul>
<li>엔티티에 소속된 인스턴스들을 구별하는 기준역할</li>
<li>유일성, 최소성, 불변성, 존재성</li>
<li>하나가 아닌 여러개일수 있음(복합키)</li>
</ul>
<h3 id="외래식별자">외래식별자</h3>
<ul>
<li>부모 식별자와 공통속성이 자식에게도 존재하면 해당 속성을 외래 식별자로 지정</li>
<li>자식 엔티티에 부모 엔티티 주식별자 공통속성이 없을 경우 자식에게 속성 추가후 외래식별자로 지정</li>
</ul>
<h3 id="엔티티간-부모-자식-관계">엔티티간 부모 자식 관계</h3>
<ul>
<li>어느쪽이 먼저 생성되야 하는가에 따라 결정</li>
<li>부모엔티티 정보가 존재해야 자식도 생성가능</li>
</ul>
<h3 id="참여도">참여도</h3>
<ul>
<li>어떤 기준이 되는 엔티티가 있을때 반드시 대응되는 엔티티가 존재해야 하면 필수, 아니면 선택</li>
</ul>
<h3 id="식별---비식별-관계">식별 - 비식별 관계</h3>
<ul>
<li>식별관계
<ul>
<li>1:N 관계에서 외래 식별자가 주식별자의 역할도 하는경우</li>
<li>실선으로 표현</li>
<li>PFK</li>
</ul>
</li>
<li>비식별관계
<ul>
<li>1:N 관계에서 외래 식별자가 단순 속성인경우</li>
<li>PF</li>
<li>점선으로 표현</li>
</ul>
</li>
</ul>
<blockquote>
<p>그냥 모든 고유 ID를 부여하면 안되나?<br>
비니지스 로직은 언제든 바뀔수 있고 이걸 엔티티 식별자로 삼을경우 비지니스 구조가 바뀌면 테이블을 다 뜯어고쳐야하는 일이 발생할 수 있음<br>
유지보수 차원에서 그냥 모든 고유 ID를 부여하는편이 훨씬 나음!<br>
고유 ID로 비식별관계로 만들것!</p>
</blockquote>
<h3 id="erd-표기법-관계">ERD 표기법( 관계)</h3>
<ul>
<li>1대1</li>
<li>1대 N</li>
<li>N 대 N
<ul>
<li>데이터 모델링에서 N대N은 미완성상태임 1대N N대1로 해소해주는게 바람직함</li>
</ul>
</li>
</ul>
<p><img src="https://github.com/jinia91/blogTest/blob/main/%EC%B9%B4%EB%94%94%EB%84%90%EB%A6%AC%ED%8B%B0.png?raw=true" alt="enter image description here"></p>
<h3 id="erd-그리기-팁">ERD 그리기 팁</h3>
<ol>
<li>부모 - 자식간 관계 설정하기</li>
<li>카디널리티 설정
<ol start="3">
<li>몇대 몇 관계?</li>
<li>다대다면 정규화해서 해소하기</li>
</ol>
</li>
<li>참여도 파악(1, 0)</li>
<li>식별 / 비식별파악(모든 고유아이디 넣고 비식별로 하기)</li>
</ol>
<h3 id="실습-1">실습 1</h3>
<p><img src="https://github.com/jinia91/blogTest/blob/main/TEST.png?raw=true" alt="enter image description here"></p>
<p><img src="https://github.com/jinia91/blogTest/blob/main/practice2.png?raw=true" alt="enter image description here"></p>

