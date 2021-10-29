---


---

<h3 id="매핑시-주의사항">매핑시 주의사항</h3>
<h3 id="enumerated">@Enumerated</h3>
<p>ORDINAL 사용 금지!</p>
<p>EnumType.STRING 이름으로 저장하는게 유지보수에 훨씬 좋음 ORDINAL로하면 위험함</p>
<h3 id="id-생성시-매핑전략-권장사항">ID 생성시 매핑전략 권장사항</h3>
<h4 id="long형--대체키-키-생성전략-사용">LONG형 + 대체키 +키 생성전략 사용</h4>
<p>주민번호니 이런 비지니스차원의 자연수는 절대 사용하지말것!</p>
<h4 id="identity-전략-특징">Identity 전략 특징</h4>
<p>DB에 ID 생성전략을 위임하는방법으로 MYSQL에서 내부 AUTO INCREMENT 사용하는것</p>
<p>이경우 PERSIST 메소드를 할때 영속성 컨텍스트의 캐시에 ID값을 앱단위에서는 알수 없으므로 PERSIST시 바로 INSERT쿼리가 날라가고 아이디값을 반환받아 영속컨텍스트 캐시에 저장하게된다.</p>
<p>메커니즘을 알아두자.</p>
<h4 id="sequence-전략-특징">SEQUENCE 전략 특징</h4>
<p>오라클 시퀸스 객체같은 개념<br>
따라서 DB 시퀸스에 쿼리를 보내서 다음값을 받아와 영속성 컨텍스트에 저장시킴!<br>
즉 IDENTITY전략과 달리 PERSIST시 쿼리가 날라가지 않음</p>
<h4 id="둘다-네트워크를-타기때문에-성능상-이슈가-있을수-있음">둘다 네트워크를 타기때문에 성능상 이슈가 있을수 있음</h4>
<p>Sequence의경우 SequenceGenerator를 통해 AllocationSize를 할당해서 다음 id값들을 미리 캐싱할수 있음! 이때 디비엔 할당 사이즈만큼 미리 시퀸스를 땡겨오므로 동시성에 문제가 생기지 않음!</p>
<h2 id="연관관계-매핑">연관관계 매핑</h2>
<h3 id="다-대-일-매핑에서-연관관계-주인정하기">다 대 일 매핑에서 연관관계 주인정하기</h3>
<p>기본적으로 rdb에서 두 개체는 FK로 연결되있음</p>
<p>즉 두 테이블에 대해 조회할때 조인으로 합쳐저서 논리적으로 하나의 테이블로 다루게됨</p>
<p>그러나 객체지향적으로 바라보면 각각의 객체는 의존성에 의해 단방향으로 흐르는 관계를 맺음</p>
<p>FK를 기준으로 테이블을 설계하게되면 다대일 관계에서 다에 해당하는 객체는 일에 해당하는 PK를 외래키로 들고있음</p>
<p>따라서 다에 해당하는 객체는 일의 객체로 참조관계를 갖지만 현재 테이블과 매핑된시점에서 일의 객체는 다의 객체로 참조관계를 갖지 못함!</p>
<p>이때 테이블에 반영은 안되지만 논리적으로 조인된 테이블에서 매핑시켜 값을 집어넣을수있는 참조객체LIST를 들고있다면</p>
<p>객체세계에서도 RDB와 같은 양방향 관계를 구현할수 있게됨</p>
<p>그리고 이때, 실제로 FK값을 관리하는 '다’의 객체는 두 객체간의 관계에서 주인이되고</p>
<p>‘일’ 에 해당하는 객체는 ‘mapped by = 다의 속성’ 로 종속됨을 표시해줘야함</p>
<p>Many 쪽이 주인!, FK를 들고있음!, 갱신도 주인만 함! one 쪽이 mapped bh</p>
<h4 id="또한">또한</h4>
<p>DB에 데이터를 집어넣을때 현실적으로 주인과 매핑된 객체 둘다에 저장값을 집어넣는게 영속성 컨텍스트 관리상 옳은 방식이고 객체지향적으로도 양쪽에 데이터값을 모두 기입하는게 옳은 방식이다</p>
<p>그냥 둘다 적어서 저장하도록 하자</p>
<h3 id="일대다-관계-매핑은-추천하지않음">일대다 관계 매핑은 추천하지않음</h3>
<p>외래키는 다 쪽 테이블에 가는 RDB특성상 직관성문제로 코드단위에서 유지보수시 매칭이 되지 않아 헤깔리게됨</p>
<p>참조문제로 일에서 다로 가는경우가 필요하다면</p>
<p>다대일 양방향관계를 쓰는 전략을 사용하는게 남</p>
<h3 id="일대일-관계">일대일 관계</h3>
<p>외래키에 유니크제약조건이 추가된 관계를 의미</p>
<p>어디를 연관관계주인으로 둘지 고민인데</p>
<p>객체지향적으로 많이 조회를 하는쪽에 주인을 두는게 좀더 편리함 DB관점에서는 NULL값을 허용하게되므로 불편하긴함… JPA의 한계 어쩔수없음</p>
<h3 id="다대다-관계">다대다 관계</h3>
<p>사용하지 말고<br>
일대다 조인테이블 다대일로 관계를 맺으며 조인테이블을 조인 객체로 승격시켜서 도메인단위에서 관리하도록 하자</p>
<p>이때 조인테이블의 PK는 전통적인 방식인 양방향 FK -&gt; 슈퍼키로 만들기보단<br>
그냥 비지니스랑 의미없는 UID를 주는것이 더 바람직함(설계의 유연성때문)</p>
<h3 id="상속관계-매핑inheritance">상속관계 매핑(Inheritance)</h3>
<ul>
<li>
<p>관계형 데이터베이스는 상속관계X</p>
</li>
<li>
<p>슈퍼타입 서브타입 관계라는 모델링 기법이 객체 상속과 유사</p>
</li>
<li>
<p>상속관계매핑 : 객체의 상속 구조와, DB의 슈퍼타입 서브타입관계를 매핑</p>
</li>
<li>
<p>실제 디비에서 구현전략</p>
<ul>
<li>JOINED 조인(DTYPE 추가 가능)</li>
<li>SINGLE_TABLE 단일테이블(DTYPE으로 구분)</li>
<li>TABLE_PER_CLASS 개별테이블</li>
<li>DTYPE은 추가하는게 좋음</li>
</ul>
</li>
<li>
<p>장단점</p>
<p>Join전략 : 정규화되어있음, 관계형 디비에 충실, 저장공간 효율화 but 조회할때 조인이 많이 사용하다보니 성능과 테이블의 복잡성 but join이 정석!</p>
<p>단일테이블 전략 : 쿼리가 단순, 테이블관리가 쉬움 / null 허용하는 단점, 무결성입장에서 애매하고 성능이 일반적으론 빠르지만 나쁠수도 …?</p>
<p>Table_Per_Class의 경우 조회시 모든 테이블을 유니온해서 다 뒤지므로 비효율적 개별 테이블은 걍 쓰지마!!</p>
</li>
</ul>
<h3 id="mappedsuperclass">MappedSuperclass</h3>
<ul>
<li>
<p>상속관계 매핑x</p>
</li>
<li>
<p>엔티티x, 테이블과 매핑x</p>
</li>
<li>
<p>부모클래스 상속받는 자식클래스에 매핑정보만 제공</p>
</li>
<li>
<p>조회, 검색불가! 상속이 아니다!</p>
</li>
<li>
<p>추상클래스로 만들기</p>
</li>
<li>
<p>테이블과 상관없고 단순히 entity 가 공통으로 사용하는 매핑 정보를 모으는 역할</p>
</li>
<li>
<p>주로 등록일, 수정일, 등록자, 수정자같은 전체 엔티티에서 공통으로 적용하는 정보를 모을 때 사용</p>
</li>
<li>
<p>참고 : @Entity 클래스는 @Entity(진짜 상속)나 @MappedSuperclass 로 지정한 클래스만 상속가능</p>
</li>
<li>
<p>BasicEntity 실무에서도 쓰자 !</p>
</li>
</ul>
<h2 id="프록시">프록시</h2>
<p>기본 제공 api중 find()와 get()이 다른 역할<br>
find는 실제 조회지만 get은 프록시 엔티티를 조회<br>
사실상 영속성 컨텍스트에 프록시 객체를 만든뒤 실제 조회되는 시점에서 쿼리를 보내는 방법</p>
<h3 id="특징">특징</h3>
<ul>
<li>프록시 객체는 처음 사용할때 한번만 초기화</li>
<li>프록시 객체가 실제 객체로 바뀌는게 아닌 프록시 내부의 커서가 실제 객체를 가르키는거임</li>
<li>따라서 타입체크시에 ==을 하게되면 다른 클래스로 판정됨!! 상속받은 자식객체임 따라서 instanceOf를 써야된다</li>
<li>영속성컨텍스트에 이미 찾는 객체가있다면 get을 써도 실제 객체로 반환 프록시x</li>
<li>
<blockquote>
<p>영속성 컨텍스트안에서 한번 캐싱된 객체는 동일 조회에 대해 항상 동일성을 유지해야하기때문</p>
</blockquote>
</li>
<li>이에 대한 응용으로 프록시 객체를 조회후, find로 동일객체를 다시 조회한다면 두 변수는 같은 프록시 객체를 지목하고 해당 프록시객체의 커서가 실제 find로 조회된 객체를 지목하는 방식으로 됨 즉 프록시객체의 껍데기는 유지!</li>
</ul>
<blockquote>
<p>핵심은 서비스로직에서 프록시가 나오든 실제 객체가 나오든 문제가 안생기도록 로직을 짜는것!</p>
</blockquote>
<ul>
<li>프록시객체가 실제객체를 찾기 이전에 트랜잭션이 끝나버리는경우 프록시 객체는 실제 객체조회가 불가능<br>
(org.hibernate.LazyInitializationException)</li>
</ul>
<h2 id="지연-로딩fetchtype-lazy">지연 로딩(FetchType =LAZY)</h2>
<ul>
<li>객체 조회시 참조하는 객체가 있으면 참조 객체는 Proxy객체를 만들어 삽입한채로 조회됨</li>
<li>이후 참조객체를 찾을경우 Proxy의 커서로 쿼리가 날라가 조회</li>
</ul>
<h3 id="반대는-즉시로딩fetchtypeeager">반대는 즉시로딩(FetchType=EAGER)</h3>
<h3 id="but-실무에선-즉시로딩-쓰면-안됨">but 실무에선 즉시로딩 쓰면 안됨!!!</h3>
<blockquote>
<p>테이블이 5개 6개 걸리면 그게 다 매번 조인될경우 성능에 지장 문제는 Default값이 즉시로딩… 즉 모든 매핑상황에서 참조부분에 lazy로 발라넣어야한다…</p>
</blockquote>
<h3 id="또한-jpql에서-n1-문제발생">또한 JPQL에서 N+1 문제발생!</h3>
<blockquote>
<p>JPQL은 조인전략으로 조인되서 나가는방식과는 달리 쌩 SQL문으로 번역되서 나가므로 SQL 쿼리가 한번 날라가고 거기에 JPA상으로 참조된 다른 테이블 N개에 대해 추가 쿼리가 N개 더 날라가는 문제</p>
</blockquote>
<h3 id="다-lazy로-발라라">다!!! LAZY로 발라라!</h3>
<h2 id="jpa-cascade">JPA CASCADE</h2>
<blockquote>
<p>일대다 매핑상황에서 Insert를 날릴때 하나의 객체를 저장하려면 참조하는(되는) 객체도 지정하거나 새로 만들어서 저장하는게 당연<br>
이때 만약 새로운 객체를 전부 만든상황이라면 각각에 persist를 날려야함<br>
이때 참조되는 객체들도 한번에 Insert해주는 기능</p>
</blockquote>
<p>ex)<br>
@OneToMany(cascade = CascadeType.ALL)</p>
<p>연관관계나 RDB개념이랑은 상관없고 그냥 Cascade 설정이 들어간 멤버변수들에 대해서도 영속성 관리를 해주는 개념</p>
<ul>
<li>ALL, PERSIST 정도만 사용<br>
사실상 집합관계일때 사용</li>
</ul>
<h2 id="고아객체">고아객체</h2>
<p>위의 CASCADE에서 부모객체와의 연관성이 사라졌을때 자식객체를 의미<br>
orpanRemoval = true;<br>
고아객체 삭제</p>
<p>=&gt; DDD의 개념중 집합관계 Root만 DAO가 관리하고 이하 자식들은 부모를 통해 생명주기를 관리하는 것과 일맥상통</p>
<h2 id="jpa가-인식하는-값-타입">JPA가 인식하는 값 타입</h2>
<ol>
<li>ENTITY</li>
<li>기본값타입
<ul>
<li>int, double, Integer, Long, String…</li>
<li>Entity에 생명주기를 의존</li>
</ul>
</li>
<li><strong>임베디드 타입(복합값타입)</strong>
<ul>
<li>두개이상을 묶어서 만들때</li>
<li>쉽게말해 클래스를 따로 뽑아내는것</li>
<li>이때 임베디드 타입은 부모 엔티티의 생명주기와 같이함</li>
<li>중요한것은 따로 테이블을 만드는것이 아니라 싱글테이블로 들어감! 객체지향적으로 관리하는것일 뿐</li>
<li>@Embeddable, @Embedded</li>
<li>@AttributeOverride 속성 재정의를 통해 한 Entity에 동일 임베디드타입을 여러개도 넣을수 있음</li>
<li>문제는 CallByReference로 참조하는거기때문에 안전하지않음</li>
</ul>
</li>
</ol>
<blockquote>
<p>공유참조 문제를 해결하기 위해서 임베디드타입은 불변객체로 생성해야한다!!!<br>
마치 String처럼 한번쓰고 버리는방식!<br>
즉 임베디드타입으로 만드는 클래스는 Setter를 안만들면됨! 생성자로 생성되는 최초에만 작성가능</p>
</blockquote>
<blockquote>
<p>값타입취급을 해줘야하기때문에 동등성비교를 위한 equals hashCode 오버라이딩 필수!</p>
</blockquote>
<ol start="4">
<li><strong>컬렉션값타입</strong>
<ul>
<li>Entity를 컬렉션 x 값을 컬렉션으로 넣을때를 말하며</li>
<li>RDB는 컬렉션을 담는방법이 테이블뿐이므로 사실상 일대다 매핑관계와 동일하게 구현</li>
<li>단 이때 모든값을 묶어서 PK로 만들어서 엔티티랑 구분하며 값컬렉션 테이블의경우 Entity가 아니므로 스스로의 생명주기(CRUD)가 없이 부모 Entity에 종속(CascadeALL이 디폴트인셈)</li>
<li>@ElementCollection<br>
@CollectionTable(name = “”, JoinColumns = @JoinColumn(name=""))을 사용하여 컬렉션값 변수에 달아주기</li>
<li>컬렉션들은 지연로딩이 디폴트</li>
<li>값타입 컬렉션에 변경사항이 발생하면 해당 컬렉션을 모두 삭제후 다시 INSERT하는 쿼리가 날라감;; <strong>쓰지마!!!</strong></li>
</ul>
</li>
</ol>
<blockquote>
<p>실무에서는 값타입컬렉션 쓰지말고 그냥 일대다 관계로쓰자</p>
</blockquote>
<h2 id="jpql-문법">JPQL 문법</h2>
<h3 id="기본적으론-sql과-동일">기본적으론 SQL과 동일</h3>
<ul>
<li>SELECT M FROM Member AS M WHERE M.age&gt;18</li>
<li>대소문자를 기본적으로 구분함!</li>
<li>FROM 뒤에는 Entity 클래스 이름으로, Select에도 전체 조회시 객체 자체를 조회</li>
<li><strong>별칭은 필수!</strong></li>
</ul>
<h3 id="typequery-query">TypeQuery, Query</h3>
<pre><code>TypeQuery&lt;Member&gt; query = 
em.createQuery("Select m From Member m", Member.class)
Query = 
em.createQuery("Select m.username, m.age From Member m", Member.class)
</code></pre>
<h3 id="쿼리안에-파라미터-사용할경우">쿼리안에 파라미터 사용할경우</h3>
<pre><code>int userageParam = 13;
createQuery(Select m from Member m where m.userage =:userage)
.query.setParameter("userage", userageParam);
</code></pre>
<h3 id="결과조회-api">결과조회 API</h3>
<ul>
<li>query.getResultList(): 결과가 하나 이상일때 리스트 반환
<ul>
<li>결과가 없으면 빈리스트 반환</li>
</ul>
</li>
<li>query.getSingleList(): 결과가 정확히 하나일경우
<ul>
<li>없거나 여러개면 에러 던짐</li>
</ul>
</li>
<li>스칼라 프로젝션으로 여러값 조회할때
<ul>
<li>select m.username, m.age from Member m</li>
<li>Query 타입으로 조회</li>
<li>Object[] 타입으로 조회 List&lt;Object[]&gt; resultList</li>
<li>new 명령어로 조회
<ul>
<li>단순값을 DTO로 바로조회하기</li>
<li>Select new jpa.jpql.UserDTO(m.username, m.age) from Member m</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="페이징-api">페이징 API</h3>
<ul>
<li>query.setFirstResult(); 어디부터</li>
<li>query.setMaxResult(); 어디까지</li>
</ul>
<h3 id="조인">조인</h3>
<ul>
<li>내부 / 외부 조인 일반 sql과 동일</li>
<li>세타 조인, 크로스 조인
<ul>
<li>select count(m) from Member m, Team t where m.username = <a href="http://t.name">t.name</a></li>
</ul>
</li>
<li>on으로 조인시 조건도 지정 가능
<ul>
<li>select from Member m join m.team t on <a href="http://t.name">t.name</a> =“A”<br>
이런식으로 조건문을 on에 실어서 쿼리 보내는것도 가능</li>
</ul>
</li>
</ul>
<h3 id="서브-쿼리-함수">서브 쿼리 함수</h3>
<ul>
<li>exists all any some 으로 참, 거짓 반환</li>
<li>SELECT M FROM Member M<br>
WHERE EXIST(SELECT T FROM M.team T WHERE <a href="http://T.name">T.name</a> = ‘A’)<br>
<strong>JPA 서브쿼리의 한계</strong> : FROM절에서 사용불가능! 조인으로 해결해야함</li>
</ul>
<h3 id="조건식">조건식</h3>
<ul>
<li>
<p>기본 CASE</p>
<pre><code>SELECT 
		WHEN M.age &lt;= then '학생요금'
		WHEN M.age &gt;= then '경로요금'
		ELSE '일반요금'
	END
FROM Member M
</code></pre>
</li>
<li>
<p>단순 CASE</p>
<pre><code>SELECT
  	CASE T.name
  		WHEN '팀A' THEN '인센티브110%'
  		WHEN '팀B' THEN '인센티브120%'
  		ELSE '인센티브 105%'
  	END
  FROM Team T		 
</code></pre>
</li>
<li>
<p>COALESCE : 하나씩 조회해서 NULL이 아닌것을 반환<br>
SELECT COALESCE (m.username, ‘이름 없는 회원’) FROM Member m;<br>
m.username확인하고 널이 없으면 그대로 m.username을 반환하지만 널이 있으면 넘어가서 ‘이름 없는 회원’ 을 조회, 리터럴이므로 null이 아니므로 해당 컬럼을 반환하게됨<br>
COALESCE(A,B,C,D,0) 이런식일경우 A,B,C,D를 차례로 조회함</p>
</li>
<li>
<p>NULLIF : 두 값이 같으면 NULL반환 , 다르면 첫번째 값 반환</p>
</li>
</ul>
<h3 id="그외에-jpa-공통-지원-기본함수">그외에 JPA 공통 지원 기본함수</h3>
<ul>
<li>CONCAT</li>
<li>SUBSTRING</li>
<li>TRIM</li>
<li>LOWER,UPPER</li>
<li>LENGTH</li>
<li>LOCATE</li>
<li>ABS,SQRT,MOD</li>
<li>SIZE, INDEX</li>
<li>디비에 종속적인 함수도 다 지원하므로 크게 걱정은 안해도됨</li>
</ul>
<h3 id="경로-표현식">경로 표현식</h3>
<ul>
<li>. 점찍어서 객체 그래프를 타고 가는것</li>
<li>이때 종류 3가지를 꼭 구분해서 알아두자
<ul>
<li>m.username 상태 필드를 탐색</li>
<li>join m.team t  단일값으로 연결된 연관(의존) 필드 탐색
<ul>
<li>대상이 엔티티</li>
</ul>
</li>
<li>join m.orders o 컬렉션으로 연결된 연관(의존) 필드 탐색
<ul>
<li>대상이 컬렉션</li>
</ul>
</li>
</ul>
</li>
<li><strong>특징</strong>
<ul>
<li>상태 필드 : 경로 탐색의 끝, .못찍음 당연</li>
<li>단일값 연관경로 : 묵시적 내부 조인 발생, 탐색 O, 탐색한 엔티티로 또 탐색 가능(. 찍고 또감)
<ul>
<li>묵시적 내부 조인은 실무에서 문제가 발생할 수 있음. 내가 원하는게 있다면 직접 조인쿼리를 짜서 하는게 맞다. 예상치못한 쿼리가 날라가서 문제발생 위험!</li>
</ul>
</li>
<li>컬렉션값 연관경로 : 묵시적 내부조인 발생, 탐색 X
<ul>
<li>
<p>묵시적 조인으론 탐색 불가능함  명시적 조인을해서 사용</p>
<pre><code>SELECT t.members FROM Team t; (x)
SELECT  m.username FROM Team t JOIN t.members m;
</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><strong>그냥 실무에선 묵시적 조인사용하지말 것 명시적 조인쓰자</strong></p>
<h2 id="페치-조인">페치 조인</h2>
<ul>
<li>SQL 조인종류 X</li>
<li>JPQL 에서 성능 최적화를 위해 제공하는 기능</li>
<li><strong>실무에서 매우중요!</strong></li>
<li>연관 엔티티나 컬렉션을 SQL한번에 함께 조회하는 기능</li>
<li>JOIN FETCH 명령어로 사용</li>
</ul>
<p>EX)<br>
SELECT m FROM Member m JOIN FETCH m.team</p>
<p>=&gt;SQL<br>
SELECT m.* , t.*<br>
FROM MEMBER m<br>
INNER JOIN TEAM t ON (M.TEAM_ID = <a href="http://T.ID">T.ID</a>);</p>
<p><strong>중요</strong></p>
<blockquote>
<p>조인된 테이블 전체에 대한 조회라고 보면 됨<br>
만약 즉시로딩으로 멤버 테이블의 모든 구성원에 대한 팀들 조회하는 쿼리를 날린다면 멤버 테이블전체를 조회하는 쿼리 + 각 팀을 조회하는 (팀갯수)N개의 쿼리가 날라가는 N+1문제가 발생함!<br>
지연로딩일지라도 최초 조회하는 멤버의 팀은 가져오지만, 이후 만나는 멤버가 다른팀일경우 해당팀만큼 쿼리가 날라가므로 결국 똑같은 N+1 문제를 직면하게 됨!<br>
이를 해결하기 위해 꼭 <strong>FETCH JOIN</strong>을 사용해야한다</p>
</blockquote>
<ul>
<li>1대 다 조인일경우(TEAM 테이블에서 MEMBER와 페치 조인해서 조회하는것)
<ul>
<li>TEAM이 중복되며 뻥튀기됨!</li>
<li>문제는 이를 디비를 통해 조회해서 객체로 가져오면서 중복뻥튀기된 객체로 가져오게됨
<ul>
<li>(멤버3명, 팀2개인 테이블에서 팀으로 객체를 페치조인해서 조회하면 팀이 3개가 나옴!)</li>
</ul>
</li>
<li>DISTINCT를 날리면 JPA차원에서 메인이 되는(여기서는 팀) 테이블의 PK의 무결성이 유지되게끔 중복성을 제거해줌
<ul>
<li>결국 조회시 팀이 2개가 나옴!</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="페치조인과-일반-조인의-차이">페치조인과 일반 조인의 차이</h3>
<p>일반 조인은 연관된 엔티티의 컬럼을 지정한게 아닌이상 엔티티 자체를 영속성 컨텍스트로 가져오질 않음. 따라서 N+1 문제를 야기할 수 있음</p>
<h3 id="페치-조인의-한계">페치 조인의 한계</h3>
<ul>
<li>
<p>페치 조인 대상에 별칭 X 주지 말것 어차피 다 불러오려고 하는건데 왜 별칭을 줘? 그냥 다 끌고올것</p>
</li>
<li>
<p>둘 이상의 컬렉션은 페치조인 X</p>
</li>
<li>
<p>컬렉션을 페치조인하면 페이징 API 사용 불가능</p>
<ul>
<li>일대다의 경우 데이터가 뻥튀기되서 안됨</li>
<li>@Batchsize 를 사용하면 해결 가능</li>
</ul>
</li>
</ul>
<p>=&gt; 실무에서는 모두 지연로딩, 최적화가 필요한곳은 페치조인을 하기</p>
<h2 id="엔티티-직접사용">엔티티 직접사용</h2>
<ul>
<li>
<p>JPQL에서 엔티티를 직접 사용한 경우 SQL에서 해당 엔티티의 기본 키값을 사용</p>
<pre><code>SELECT COUNT(M.ID) FROM MEMBER M // 아이디사용
SELECT COUNT(M) FROM MEMBER M // 엔티티 자체
</code></pre>
</li>
</ul>
<p>둘다 완전히 똑같음</p>
<p>둘다 m.id로 날라감 엔티티라도 id 기본키값으로</p>
<h2 id="네임드-쿼리">네임드 쿼리</h2>
<ul>
<li>미리 정의해서 이름을 부여해두고 사용하는 정적 쿼리</li>
<li>앱 로딩시점에 쿼리를 검증하고 캐싱해둠 =&gt; 로딩시점에 문법오류를 잡아주는 장점!</li>
</ul>
<h2 id="벌크연산">벌크연산</h2>
<ul>
<li>
<p>한번에 여러 SQL 쿼리를 날리는 방법 UPDATE DELETE INSERT</p>
<pre><code>em.createQuery("UPDATE Product p SET p.price * 
1.1 WHERE p.stockAmount &lt; : stockAmount;", 10).excuteUpdate();
</code></pre>
</li>
<li>
<p>영속성 컨텍스트를 무시하고 데이터베이스에 바로 직접 쿼리를 날리므로 벌크 연산을 먼저 실행하거나 벌크연산하고 영속성컨텍스트를 초기화할 것!</p>
</li>
<li>
<p>생각해보면 당연한게 쿼리연산시 쿼리 이전에 영속성컨텍스트를 플러시하고 이후 쿼리가 날라가면 영속성컨텍스트안에있는 엔티티들은 갱신이 안되있음</p>
</li>
</ul>

