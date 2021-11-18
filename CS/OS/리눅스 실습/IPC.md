---


---

<h2 id="ipcs">IPCS</h2>
<ul>
<li>리눅스에서 현재 사용되고있는 IPC 들을 표시해주는 명령어
<ul>
<li>메시지큐</li>
<li>공유메모리</li>
<li>세마포어</li>
</ul>
</li>
</ul>
<h2 id="파이프">파이프</h2>
<ul>
<li>
<p>기본 파이프는 단방향 통신</p>
</li>
<li>
<p>fork()로 자식프로세스 만들었을때 부모와 자식간 통신</p>
<ul>
<li>부모에서 자식으로만 가능</li>
</ul>
</li>
<li>
<p>pipe() 시스템 콜</p>
<ul>
<li>인자로 2칸짜리 배열을 받음
<ul>
<li>int fd[2];</li>
<li>pipe(fd);</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>-코드 예시</p>
<pre><code>char* msg = "Hello Child";
int main()
{
        char buf[255];
        int fd[2], pid, nbytes;
        if(pipe(fd) &lt; 0)
                exit(1);
        pid = fork();
        if(pid&gt;0){
                printf("parend pid:%d, child pid:%d\n", getpid(), pid);
                write(fd[1], msg, MSGSIZE);
                exit(0);
        }
        else {
                printf("child PID:%d\n", getpid());
                nbytes = read(fd[0], buf, MSGSIZE);
                printf("%d %s\n", nbytes,buf);
                exit(0);
        }
        return 0 ;
}
</code></pre>
<h2 id="메시지-큐">메시지 큐</h2>
<ul>
<li>
<p>msqid : 메시지큐 생성</p>
<ul>
<li>ftok() 함수로 key 생성
<ul>
<li>(패스경로, 숫자값) 인자로 키생성하므로 패스 경로 삭제나 재생성시엔 inode값이 달라져서 이전과 다른 키값을 반환하는거 염두</li>
</ul>
</li>
<li>msqid = msgget(key, msgflg); // key는 1234, msgflg는 옵션</li>
</ul>
</li>
<li>
<p>msgflg 설정</p>
<ul>
<li>예시 : IPC_CREAT : 새로운 키면 식별자 새로 생성
<ul>
<li>IPC_CREAT|0644</li>
</ul>
</li>
</ul>
</li>
<li>
<p>msgsnd() : 메시지 전송</p>
</li>
<li>
<p>msgrcv() : 메시지 수신</p>
</li>
<li>
<p>msgctl() : 메시지큐 리소스 닫기</p>
</li>
<li>
<p>코드 예시</p>
<pre><code>  msqid = msgget(1234, IPC_CREATE|0644); // 메시지큐 얻어서
  msgsnd(msqid, &amp;sbuf, buf_length, IPC_NOWAIT); // 메시지 보내기
  msgrcv(msqid, &amp;rbuf, MSGSZ, 1,0); // 숫자부분은 타입과 설정
</code></pre>
</li>
</ul>
<h2 id="공유-메모리">공유 메모리</h2>
<ul>
<li>
<p>노골적으로 kernel 공간에 메모리 공간을 만들고, 해당 공간을 변수처럼 쓰는 방식</p>
</li>
<li>
<p>message queue 처럼 fifo 방식이 아니라 해당 메모리 주소를 마치 변수처럼 접근</p>
</li>
<li>
<p>메시지큐처럼 공유메모리 key를 가지고 여러 프로세스가 접근 가능</p>
</li>
<li>
<h4 id="공유-메모리-생성">공유 메모리 생성</h4>
<ul>
<li>int shmget(key_t key, size_t size, int shmflg</li>
</ul>
</li>
<li>
<h4 id="공유-메모리-연결">공유 메모리 연결</h4>
<ul>
<li>void *shmat(int shmit, const void *shmaddr, int shmflg);</li>
</ul>
</li>
<li>
<h4 id="공유-메모리-해제">공유 메모리 해제</h4>
<ul>
<li>int shmdt(char *shmaddr);</li>
</ul>
</li>
<li>
<h4 id="읽기--쓰기">읽기 / 쓰기</h4>
<ul>
<li>printf("%s", (char *)shmaddr)</li>
<li>scrcpy((char *) shmaddr, “text asdfadf”)</li>
</ul>
</li>
</ul>
<p>-#### 공유 메모리 삭제<br>
-shmctl()</p>
<h2 id="시그널">시그널</h2>
<ul>
<li>유닉스에서 30년이상 사용된 전통적 기법</li>
<li>커널 또는 프로세스에서 다른프로세스에 어떤 이벤트가 발생되었는지를 알려주는 기법
<ul>
<li>IPC기법보다 더 광범위한 개념</li>
</ul>
</li>
</ul>
<blockquote>
<p>Ctrl + C 눌러서 프로세스 종료시키기<br>
Ctrl + Z 누르면 프로세스 백그라운드로 바꾸기</p>
</blockquote>
<h3 id="주요-시그널">주요 시그널</h3>
<ul>
<li>SIGKILL : 프로세스를 죽여라(슈퍼 관리자가 사용하는 시그널)</li>
<li>SIGALARM : 알람 발생</li>
<li>SIGSTP : 프로세스를 멈춰라</li>
<li>SIGCONT : 멈춘 프로세스 시작</li>
<li>SIGINT : 프로세스에서 인터럽트를 보내 프로세스 죽이기</li>
<li>SIGSEGV : 프로세스가 다른 메모리영역 침범</li>
<li>SIGUSR1,2 : 재정의 가능한 비어있는 시그널 &lt; - IPC기법으로 사용</li>
</ul>
<h3 id="시그널-재정의">시그널 재정의</h3>
<ul>
<li>signal(시그널시스템콜, 함수); // 특정시그널을 함수로 대신실행하는뜻</li>
</ul>
<h3 id="프로세스와-시그널">프로세스와 시그널</h3>
<ul>
<li>PCB에서 해당 프로세스가 블록 또는 처리해야할 시그널 관련 정보 관리
<ul>
<li>pending : 시그널 대기열</li>
<li>blocked : 64비트 구조체 = 시그널의 종류가 64개이며, 어떤 시그널인지를 체크하는 비트마스크</li>
</ul>
</li>
</ul>

