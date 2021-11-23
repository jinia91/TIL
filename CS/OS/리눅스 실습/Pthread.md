---


---

<h2 id="pthread">PTHREAD</h2>
<ul>
<li>thread 표준 API
<ul>
<li>Posix 스레드 또는 Pthread(피 - 쓰레드) 라고 부름</li>
</ul>
</li>
<li>Pthread API
<ul>
<li>저수준 API로 100여개의 함수 제공</li>
<li>복잡하지만, 유닉스 시스템 핵심 스레딩 라이브러리</li>
<li>다른 스레딩 솔루션도 결국 Pthread를 기반으로 구현되어 있으므로, 익혀둘 가치있다!</li>
</ul>
</li>
</ul>
<h3 id="pthread-라이브러리">Pthread 라이브러리</h3>
<ul>
<li>
<p>&lt;pthread.h&gt; 헤더 파일에 정의, 인클루드 필수</p>
</li>
<li>
<p>모든 함수는 pthread_로 시작</p>
</li>
<li>
<p>크게 두가지 그룹</p>
<ul>
<li>스레드 관리 : 생성 종료 조인 디태치등</li>
<li>동기화 : 뮤텍스(상호배제) 등 동기화 관련 함수</li>
</ul>
</li>
<li>
<p>컴파일시 gcc -pthread 로 옵션을 반드시 넣어줘야함</p>
<ul>
<li>glibc 기본 컴파일 라이브러리가 아닌 libpthread라이브러리에 구현되있으므로 플러그인개념으로 명시적 옵션 필요</li>
</ul>
</li>
</ul>
<h3 id="스레드-생성--종료">스레드 생성 / 종료</h3>
<ul>
<li>생성
<ul>
<li>int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(start_routine)(void *), void *arg)
<ul>
<li>pthread_t *thread : 식별자</li>
<li>attr_t : 특성 지정</li>
<li>start_routine : 분기시켜 시행할 함수</li>
<li>arg : 앞의 함수에 들어갈 인자</li>
</ul>
</li>
</ul>
</li>
<li>종료
<ul>
<li>void pthread_exit(void *retval);</li>
</ul>
</li>
</ul>
<h3 id="스레드-조인">스레드 조인</h3>
<ul>
<li>int pthread_join(pthread_t thread, void **thread_return);</li>
<li>pthread 식별자를 가진 스레드가 종료될때까지 기다리고 종료된 값을 리턴받음</li>
<li>리소스 해제를 해주므로 아래 detach 둘중 하나는 반드시 써야함</li>
</ul>
<h3 id="스레드-디태치">스레드 디태치</h3>
<ul>
<li>해당 스레드가 종료될경우 즉시 관련 리소스를 해제
<ul>
<li>pthread_join 를 기다리지 않고, 종료 즉시 리소스 해제</li>
<li>detach가 선언되었더라도 메인 스레드는 계속 진행되고 단순히 리소스 해제 구문역할</li>
<li>메모리 관리차원에서 존재하는 수동 리소스 해제 코드라고 이해하면됨</li>
</ul>
</li>
</ul>
<h4 id="pthread-뮤텍스---상호배제-기법">Pthread 뮤텍스 - 상호배제 기법</h4>
<ul>
<li>뮤텍스 선언과 초기화
<ul>
<li>pthread_mutex_t mutex_lock = PTHREAD_MUTEX_INITIALIZER;</li>
</ul>
</li>
<li>뮤텍스 락 걸기 / 풀기
<ul>
<li>int pthread_mutex_lock(pthread_mutex_t *mutex);</li>
<li>int pthread_mutex_unlock(pthread_mutex_t *mutex);</li>
</ul>
</li>
</ul>

