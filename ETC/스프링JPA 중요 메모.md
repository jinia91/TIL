---


---

<h2 id="공통-인터페이스">공통 인터페이스</h2>
<ul>
<li>스프링 JPA에서 기본적으로 제공해주는 공통 쿼리 메소드 	인텔리제이에서 메소드 뒤지면 왠만한기능은 다있다!</li>
</ul>
<h2 id="쿼리-메소드">쿼리 메소드</h2>
<p><a href="https://docs.spring.io/spring-data/jpa/docs/2.5.6/reference/html/#jpa.query-methods.query-creation">공식 DOC</a></p>
<p>메소드 명만으로 쿼리 자동생성하는 방법</p>
<ul>
<li>
<p>조회 : find…By…,read…By…,get…By…</p>
</li>
<li>
<p>Count : count…By 반환타입 long</p>
</li>
<li>
<p>삭제 : delete…By, remove…By 반환타입 long</p>
</li>
<li>
<p>distinct : findDistinct, findMemberDistinctBy</p>
</li>
<li>
<p>LIMIT : findFirst3, findFirst, findTop, findTop3</p>
</li>
<li>
<p>복잡한 쿼리엔 사용하기 힘들고 자잘한 쿼리들을 대체가능</p>
</li>
</ul>
<h2 id="네임드-쿼리와-리포지토리-쿼리">네임드 쿼리와 리포지토리 쿼리</h2>
<h3 id="네임드쿼리">네임드쿼리</h3>
<ul>
<li>
<p>실무에선 안씀</p>
</li>
<li>
<p>엔티티 도메인에 네임드쿼리를 작성하고 이를 불러와서 사용하는 방식</p>
</li>
<li>
<p>쿼리메소드보다 우선순위 높음</p>
</li>
<li>
<p><strong>첫 런타임시 에러를 잡아주는 장점이 존재 근데 리포지토리 쿼리도 가능해서…</strong></p>
</li>
</ul>
<h3 id="리포지토리-쿼리노네임드-쿼리">리포지토리 쿼리(노네임드 쿼리)</h3>
<ul>
<li>
<p>마이바티스 어노테이션처럼 쓰면 됨!</p>
</li>
<li>
<p>네임드쿼리의 장점은 모두 갖고 엔티티에 쿼리를 작성할필요도 없기때문에 실무에선 이걸 쓰자</p>
<pre><code>@Query("select m from Member m where m.username =:username and m.age = :age")
List&lt;Member&gt; finduser(@Param("username") String username, @Param("age") int age);
</code></pre>
</li>
</ul>
<h2 id="dto로-조회하기">DTO로 조회하기</h2>
<h3 id="쿼리-메소드-dto-조회">1. 쿼리 메소드 dto 조회</h3>
<p>그냥 반환값을 바꾸면 해결<br>
대신 이름이 매핑잘 되있어야함</p>
<p>또는 인터페이스에</p>
<p> List…</p>
<p>하지만 join 이 연결된 엔티티들에대해서는 최적화가 안되므로 복잡한 쿼리로 dto받기엔 한계가 있음</p>
<h3 id="jpql-dto-조회">2. jpql dto 조회</h3>
<pre><code>  @Query("select m.username, t.name from Member m join m.team t")
  List&lt;MemberDTO&gt; findMemberDto;
</code></pre>
<p>이렇게 하면 안됨…</p>
<pre><code>@Query("select m.username, t.name...) // 여기를
@Query("select new 패키지명.전부.MemberDto(m.username, t.name) from...) // 여기를
</code></pre>
<p>마치 생성자로 생성하듯 쿼리에서 new 를 써서 매핑되는 값들을 넣어주고 반환</p>
<p>이런거도 실무에선 걍 쿼리DSL로 쓰자</p>
<h2 id="스프링-jpa에서-반환값-중요">스프링 JPA에서 반환값 중요!</h2>
<p>List로 반환값을 받을경우 만약 반환되는 건수가 0건이라면 null로 반환되는게 아니라 empty로 반환되는 null safety 기능 을 제공</p>
<p>즉 비지니스 코드에서 != null 과같은 방식으로 코드를 짜면 에러!! size() != 0 과같이 짜야한다</p>
<p>but 단건조회는 예외는 뜨지 않지만 null이 뜸	<br>
=&gt; 단건조회는 안전하게 Optional을 쓰자</p>
<h2 id="스프링-jpa-페이징">스프링 jpa 페이징</h2>
<p>스프링 data 차원에서 페이징 객체도 기본으로 제공!(커서페이징은 아님)</p>
<p>Repository</p>
<pre><code>Page&lt;Member&gt; findByAge(int age, Pageable pageable);	
</code></pre>
<p>Pageable 객체를 넘기면 페이지와 속하는 튜플들이 반환!</p>
<p>PageRequest.of(page, size, sort형식) 으로 반환된 객체가 Pageable이므로 이걸 반환하면 됨</p>
<p>그외에도 Page에는 다양한 유틸 메소드를 제공하므로 더이상 페이지 Criteria 객체 생성 안하고도 온갖것들 다 가능하다!!!</p>
<h3 id="토탈카운트-쿼리-분리법">토탈카운트 쿼리 분리법</h3>
<p>오프셋 쿼리에서 토탈카운트 쿼리 계산은 데이터가 클수록 성능저하 리스크가 큼<br>
지난번 토이프로젝트에서 게시물 insert/delete시 트리거로 토탈카운트만 따로 계산해 정적db 데이터로 저장하고 이를 조회함으로써 트러블슈팅을 했는데<br>
데이터 JPA를 쓸경우 기본 제공되는 토탈카운트 쿼리를 분리함으로서 위와같은 커스텀을 적용할수 있다!</p>
<ul>
<li>방법</li>
</ul>
<p>Repository</p>
<pre><code>@Query(value = "select m from Member m, countQuery = "select count(m.username)" from Member m")
Page&lt;Member&gt; findByAge(int age, Pageable pageable);	
</code></pre>
<p>여기서 카운트 쿼리를 이전 토이프로젝트처럼 별도의 카운트 데이터로 관리하는걸 조회시켜서 성능을 훨씬 끌어올릴수 있음!</p>
<p>+@ sort도 이런방식으로 분리해서 가능</p>
<h3 id="slice">Slice</h3>
<p>무한스크롤용 더보기 페이징으로<br>
limit +1  쿼리를 날려서 존재할경우 더보기 버튼 생성케해서 하는방식.<br>
토탈카운트를 계산하는방식이 아니므로 성능상 이점이 생김</p>
<h3 id="사용시-설정법">사용시 설정법</h3>
<p>야멀에<br>
data web pageable에서<br>
default - page - size<br>
max - page - size<br>
로 설정가능</p>
<p>혹은</p>
<p>컨트롤러에서 인자를 받을 때<br>
@PageableDefault(size, sort… )</p>
<p>설정 가능</p>
<h3 id="page-객체안의-조회된-엔티티-객체들을-매핑시키는-기본-메소드-제공">Page&lt;&gt; 객체안의 조회된 엔티티 객체들을 매핑시키는 기본 메소드 제공!</h3>
<p>page.map(member -&gt; new MemberDto(member.getUsername,…));</p>
<h2 id="벌크성-업데이트-쿼리">벌크성 업데이트 쿼리</h2>
<p>배치 insert 개념인데 GenerateType.Identity에선 작동 안함 알아두자</p>
<p>Sequence 타입에서도 배치 채번을 통해 번호를 당겨와야 성능 최적화가 됨.</p>
<pre><code>@Modifying
@Query("update Member m set m.age = m.age+1 where m.age &gt;= : age")
int bulkAgePlus(@Param("age") int age);
</code></pre>
<p>JPA는 영속성 컨텍스트를 이용하지만 위의 벌크성 쿼리는 쿼리가 직접 날라가 수정을 때리므로 영속성 컨텍스트에 영향을 못줌.</p>
<p>따라서 벌크성 업데이트 쿼리를 사용할경우 영속성 컨텍스트를 비워주거나 트랜잭션 처음에 날려야함 유의할것!</p>
<pre><code>@Modifying(clearAutomatically = true)
@Query("update Member m set m.age = m.age+1 where m.age &gt;= : age")
int bulkAgePlus(@Param("age") int age);
</code></pre>
<p>유지보수에 위의 방식이 더 좋으므로 이걸로 쓰자!</p>
<h2 id="엔티티-그래프">엔티티 그래프</h2>
<p>페치조인을 쿼리 없이 날리는 방법</p>
<pre><code>@Override
@EntityGraph(attributePaths = {"team"})
List&lt;Member&gt; findAll();
</code></pre>
<p>@EntityGraph 애너테이션에서 지정한 속성을 페치조인해서 조회</p>
<p>@Query 위에 @EntityGraph 애너테이션을 붙여서 jpql에 페치조인을 추가도 가능</p>
<h2 id="jpa-힌트">JPA 힌트</h2>
<p>JPA 구현체인 하이버네이트에게 힌트를 날려 추가적인 기능을 사용할때 쓰는 방법</p>
<pre><code>@QueryHints(value = @QueryHint(name = "org.hibernate.readOnly", value = "true"))
Member findReadOnlyByUsername(String username);
</code></pre>
<p>org.hibernate.readOnly 변경감지를 안하는 detach 기능 조회된객체는 영속성관리대상이 아님</p>
<h2 id="리포지토리-커스텀">리포지토리 커스텀</h2>
<ul>
<li>기본적으로 공통 Interface 를 정의하면 구현체는 스프링 데이터가 자동생성해줌</li>
<li>여기서 특정기능을 넣기위해 구현체를 직접 만들기엔 불가능!</li>
<li>QueryDsl 라이브러리 추가, 마이바티스 추가 등등을 하기위한 방법으로 리포지토리 커스텀방법을 제공</li>
</ul>
<h3 id="방법">방법</h3>
<ol>
<li>추가 기능을 가진 interface를 따로 정의<br>
ex) MemberRepositoryCustom</li>
<li>해당 인터페이스의 구현체 클래스를 개발
<ul>
<li>이름 제약이 존재</li>
<li>MemberRepositoryImpl</li>
<li>xml설정으로 바꿀수는 있지만… CoC를 따르자</li>
</ul>
</li>
<li>해당 인터페이스를 원래 사용하는 인터페이스에 다중상속<br>
ex) MemberRepository extends JpaRepository&lt;Member,Long&gt;, MemberRepositoryCustom</li>
</ol>
<blockquote>
<p>practice tip<br>
핵심 비지니스 로직의 리포지토리와 화면렌더링을 위한 복잡한 쿼리의 리포지토리 메소드부분은 분리해서 복잡도를 낮추고 유지보수를 올리는 방법도 존재<br>
굳이 하나의 리포지토리에 책임을 다 부가해 모듈을 비대하게 만들필요가 없다!</p>
</blockquote>
<h2 id="auditing">AUDITING</h2>
<ul>
<li>
<p>엔티티 생성, 변경시 이를 트랙킹하는것</p>
<ul>
<li><strong>등록일 수정일</strong>
<ul>
<li><strong>운영을 위해 무조건 하자! 없으면 지옥!!</strong></li>
<li>모든 변경가능 테이블에 등록일 수정일은 넣도록하자</li>
<li>만약없다면 로그를 뒤지면됨… 근데 언제 뒤지고 앉아있을래?</li>
<li>로그는 최후의 수단일뿐</li>
</ul>
</li>
<li><strong>등록자 수정자</strong></li>
<li>4가지는 실무에서 기본적으로 깔고가는편</li>
</ul>
</li>
<li>
<p>JPA 단위에서 사용(복습)<br>
- BaseEntity 추상클래스를 만들어 상속</p>
<pre><code>  @MappedSuperclass
  public abstract class BaseEntity {  

  @Column(updatable = false)  
  private LocalDateTime createdDate;  
  private LocalDateTime updatedDate;  


  @PrePersist  
public void prePersist(){  
      createdDate = LocalDateTime.now();  
      updatedDate = LocalDateTime.now();  

  }  

  @PreUpdate  
public void preUpdate(){  
      updatedDate = LocalDateTime.now();  
  }
</code></pre>
</li>
</ul>
<p>이후 모든 객체에 상속하면됨</p>
<blockquote>
<p>상속관계가 아니라 단순히 공통된 요소를 추가해주는 매핑이라 생각해야함! 엔티티 상속관계랑은 다름</p>
</blockquote>
<p>but<br>
스프링 데이터 jpa를 사용하면 더 유용한기능 존재!</p>
<ul>
<li>
<p>@EnableJpaAuditing을 앱클래스에 부착</p>
<pre><code>  @EntityListeners(AuditingEntityListener.class)  
  @MappedSuperclass  
  @Getter  
  public abstract class BaseEntity {  
    
      @CreatedDate  
   @Column(updatable = false)  
      private LocalDateTime createdDate;  
     
      @LastModifiedDate  
    private LocalDateTime updatedDate;  
        
  }
</code></pre>
</li>
<li>
<p>createdby , updatedby도 가능!</p>
<ul>
<li>AuditorAware auditorProvider() 를 빈등록하여 세션에서 아이디를 꺼내오게하면됨</li>
</ul>
</li>
</ul>
<h2 id="save-와-머지">SAVE() 와 머지</h2>
<p>스프링 JPA에서 제공하는 인터페이스중 save()는 인자로 넘어온 엔티티가 준영속 엔티티인경우 머지를 해줌</p>
<p>만약 내가 persist하려는 엔티티가 id값을 가질경우 jpa는 이를 준영속엔티티로 인식해서 조회후 더티체킹하는 머지를 하려하고 셀렉으로 끄집어낼 수 없으며 이후 저장을 함<br>
즉 select 쿼리가 한번 더 날라가므로 성능상 문제가 생김</p>
<p>또한 머지는 데이터 무결성 정합성에 문제를 야기할 수 있으므로 업데이트는 더티체킹으로 해결함이 옳으며 실무에서 머지는 그냥 쓰지 말것</p>
<p>save()도 업데이트 용도로 쓰지말자!</p>
<p>또한 generatedId 전략을 사용하지 않는 id의 경우 직접 식별자를 입력해야하는데 이때도 merge가 호출됨을 막기위해<br>
persistable 과 createdDate를 사용하는 방법도 고려해보자</p>
<h2 id="네이티브-쿼리-사용">네이티브 쿼리 사용</h2>
<h3 id="쿼리-애너테이션">1. 쿼리 애너테이션</h3>
<pre><code>@Query("slect * form member where username = ?", nativeQuery =true)
	Member bulkAgePlus(@Param("username") String username);
</code></pre>
<p>하지만 반환타입 지원이 안되거나 셀렉 할때 일일히 다 적어야한다거나 등등  실무에서 쓰기엔 한계가 많음</p>
<h3 id="리포지토리-커스텀-or-jpa가-관리하지-않는-별도의-jdbc-리포지토리-개발권장">2. 리포지토리 커스텀 or jpa가 관리하지 않는 별도의 jdbc 리포지토리 개발(권장)</h3>
<h3 id="그냥-쿼리dsl-정도로-쓰자매우-권장">그냥 쿼리dsl 정도로 쓰자(매우 권장)</h3>
<h2 id="참조">참조</h2>
<blockquote>
<p>DTO는 엔티티를 봐도 되지만 엔티티는 DTO를 봐선 안됨!<br>
만약 빌더를 직접 만든다면 DTO에 만들기</p>
</blockquote>
<blockquote>
<p>RESTAPI를 만들때 컨트롤러에서 반환은 반드시!! DTO로 할것 엔티티로 반환하면 화면단 렌더링과 내부 비지니스 로직간 생명주기 사이클의 불일치로 유지보수하기 극심하게 힘들게됨</p>
</blockquote>

