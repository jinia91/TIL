---


---

<h2 id="논리적-모델링이란">논리적 모델링이란</h2>
<p>현실세계 -&gt; ERD (개념적 모델링)<br>
ERD -&gt; 정규화통해 테이블 상세화(논리적 모델링)</p>
<h2 id="정규화">정규화</h2>
<ul>
<li>
<p>데이터 모델링의 목적</p>
<ul>
<li>데이터가 중복되는 현상 -&gt; 애플리케이션으로 해결</li>
<li>SQL응답속도 저하 -&gt; SQL 튜닝</li>
<li>하지만 근본적인 이유는 테이블 설계에 있는 경우도 많음 따라서 정규화를 통해 사전에 최적화를 시켜놓는것!</li>
</ul>
</li>
<li>
<p>정규화란?<br>
관계형 DB에서 데이터를 구조화하는 작업(중복을 찾아 제거)<br>
데이터의 중복을 방지하고 효율적으로 데이터를 저장하며 삽입 삭제 갱신이상의 발생을 줄이기 위함</p>
</li>
<li>
<p>정규화 과정</p>
<ul>
<li>
<p>두부이걸다줘</p>
</li>
<li>
<p><strong>1정규화</strong> : 원자값 보장</p>
<ul>
<li>하나의 속성에 여러 값 들어오면 안됨!</li>
</ul>
</li>
<li>
<p><strong>2정규화</strong> : 부분 함수적 종속 제거, 키가 아닌 모든 속성이 기본키 그룹에 완전히 함수적 종속(??)</p>
<ul>
<li>주식별자가 아닌 속성중에서 주식별자 전체가 아닌 일부 속성에 종속된 속성을 찾아 제거(속성이 복합키중 하나에만 종속되는경우 해당속성을 테이블로 따로 빼내는것 	)</li>
</ul>
</li>
<li>
<p><strong>3정규화</strong> : 이행적 함수적 종속 제거, 키가 아닌 모든 속성이 기본키에 직접 종속 (??)</p>
<ul>
<li>주식별자를 제외한 속성들중에서 종속관계가 발생하는경우 종속속성을 테이블로 빼내는것</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>실무에선 3차정도까지만 해도 무방</p>
<h3 id="nn-관계-해소법">N:N 관계 해소법</h3>
<ol>
<li>릴레이션 엔티티를 통해 1:N , N:1로 해석</li>
<li>임의로 부모엔티티를 선정(2차 정규화)</li>
</ol>
<h3 id="정규화-실습">정규화 실습</h3>
<p><img src="https://github.com/jinia91/blogTest/blob/main/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28209%29.png?raw=true" alt="enter image description here"></p>
<p><img src="https://github.com/jinia91/blogTest/blob/main/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%28210%29.png?raw=true" alt="enter image description here"></p>
<p><img src="https://github.com/jinia91/blogTest/blob/main/%EC%A0%9C2%20%EC%A0%95%EA%B7%9C%ED%99%94.png?raw=true" alt="enter image description here"></p>
<h3 id="정규화가-필요없는-설계기법">정규화가 필요없는 설계기법</h3>
<ul>
<li>장부나 전표에서 머리부와 서술부는 별도의 엔티티로 저장</li>
<li>코드 - 코드값의 관계에 있는 속성들은 별도의 엔티티로 구성한다</li>
</ul>
<h3 id="종합-실습">종합 실습</h3>
<p><img src="https://github.com/jinia91/blogTest/blob/main/%EC%A2%85%ED%95%A9%EC%8B%A4%EC%8A%B5%20%281%29.png?raw=true" alt="enter image description here"></p>

