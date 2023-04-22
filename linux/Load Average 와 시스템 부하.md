# Load Average의 정의
> the first three field in this file are load average figures giving the number of jobs in the run queue(R) or waiting for disk I/O (D) average over 1,5,15minute
> - man proc

- 코어수에 따라 LA 의 값이 의미하는 바는 다름

# Load Average 계산 과정 알아보기

1. uptime?

<img width="514" alt="image" src="https://user-images.githubusercontent.com/85499582/233761721-63c51e0b-b9e9-4f08-9cb0-a8c49e00249a.png">


- top과 함께 load average 를 볼 수 있는 명령어

2. strace 로 uptime시 스택 덤프 뜨기

    strace -s 65535 -fto uptime_dump uptime

<img width="1285" alt="image" src="https://user-images.githubusercontent.com/85499582/233761939-1ea6d6d1-df40-4656-aa42-20e0e880e925.png">
 
 3. 하단부 open?

        5404  04:13:20 openat(AT_FDCWD, "/proc/loadavg", O_RDONLY) = 4 -- proc/loadavg를 읽기 전용으로 열기 -> 파일 디스크립터는 int 4
        5404  04:13:20 lseek(4, 0, SEEK_SET)    = 0  -- int4 파일 디스크립터에 대한 파일 오프셋을 위치 0으로 이동
        5404  04:13:20 read(4, "0.04 0.10 0.06 1/496 5404\n", 8191) = 26  -- 파일 디스크립터 4에서 26바이트 읽기
        5404  04:13:20 fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0 -- 파일 디스킯터 1의 상태 얻기
        5404  04:13:20 mmap(NULL, 65536, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xffffb34f6000 -- 메모리 매핑, 시작 주소 반환
        5404  04:13:20 write(1, " 04:13:20 up 10 min,  0 users,  load average: 0.04, 0.10, 0.06\n", 63) = 63 -- load average 값들을 63바이트 문자열 작성
        5404  04:13:20 close(1)                 = 0  -- 파일디스킯터 1 close
        5404  04:13:20 munmap(0xffffb34f6000, 65536) = 0 -- 메모리 매핑 해제
        5404  04:13:20 close(2)                 = 0 -- 파일 디스크립터 2 닫기
        5404  04:13:20 exit_group(0)            = ?  -- 프로세스 종료
        5404  04:13:20 +++ exited with 0 +++
        
 결국 uptime은 /proc/loadavg 파일을 읽어서 그냥 출력해주는 역할
 계산은 그럼 누가하지?
 
 
 4. /proc/loadavg 확인해보자

<img width="393" alt="image" src="https://user-images.githubusercontent.com/85499582/233762600-cd3bea28-9939-407e-b31e-fca177f1874c.png">

- 해당 내용은 fs/proc/loadavg.c 안의 loadavg_proc_show() 함수로

      static int loadavg_proc_show(struct seq_file *m, void *v)
      {
	      unsigned long avnrun[3];  -- long 타입 3개 짜리 배열
 
       	get_avenrun(avnrun, FIXED_1/200, 0);  -- 배열 값 입력
 
       	seq_printf(m, "%lu.%02lu %lu.%02lu %lu.%02lu %ld/%d %d\n",   -- 출력
 	      	LOAD_INT(avnrun[0]), LOAD_FRAC(avnrun[0]),
 		      LOAD_INT(avnrun[1]), LOAD_FRAC(avnrun[1]),
       		LOAD_INT(avnrun[2]), LOAD_FRAC(avnrun[2]),
 	      	nr_running(), nr_threads,
 		      task_active_pid_ns(current)->last_pid);
 	      return 0;
      }



 이런식으로 소스코드를 쭉 타고가다보면
> 이런식으로 소스코드를 쭉 타고가다보면
calc_global_load(void) 함수를 찾을수 있음


<img width="712" alt="image" src="https://user-images.githubusercontent.com/85499582/233763967-9ce57b88-0fe2-41c2-9cad-83e930db72e3.png">

    void calc_global_load(void)
    {
      unsigned long sample_window;
      long active, delta;

      sample_window = READ_ONCE(calc_load_update);
      if (time_before(jiffies, sample_window + 10))
        return;

      /*
       * Fold the 'old' NO_HZ-delta to include all NO_HZ CPUs.
       */
      delta = calc_load_nohz_read();
      if (delta)
        atomic_long_add(delta, &calc_load_tasks);

      active = atomic_long_read(&calc_load_tasks);
      active = active > 0 ? active * FIXED_1 : 0;

      avenrun[0] = calc_load(avenrun[0], EXP_1, active);
      avenrun[1] = calc_load(avenrun[1], EXP_5, active);
      avenrun[2] = calc_load(avenrun[2], EXP_15, active);

      WRITE_ONCE(calc_load_update, sample_window + LOAD_FREQ);

      /*
       * In case we went to NO_HZ for multiple LOAD_FREQ intervals
       * catch up in bulk.
       */
      calc_global_nohz();
    }

<img width="637" alt="image" src="https://user-images.githubusercontent.com/85499582/233764289-bd0cd270-7903-4915-a8c3-e32871836449.png">


    void calc_global_load_tick(struct rq *this_rq)
    {
      long delta;

      if (time_before(jiffies, this_rq->calc_load_update))
        return;

      delta  = calc_load_fold_active(this_rq, 0);
      if (delta)
        atomic_long_add(delta, &calc_load_tasks);

      this_rq->calc_load_update += LOAD_FREQ;
    }



<img width="710" alt="image" src="https://user-images.githubusercontent.com/85499582/233764120-47b80f3f-fa97-4080-a5b4-094ce5213667.png">


    long calc_load_fold_active(struct rq *this_rq, long adjust)
    {
      long nr_active, delta = 0;

      nr_active = this_rq->nr_running - adjust;  -- run queue 기준으로 running 상태의 프로세스 개수 할당
      nr_active += (int)this_rq->nr_uninterruptible;  -- nr_uninterruptible(D) 상태의 프로세스 +

      if (nr_active != this_rq->calc_load_active) {
        delta = nr_active - this_rq->calc_load_active;
        this_rq->calc_load_active = nr_active;
      }

      return delta;
    }


Tick 주기마다 run queue에 있는 R, D 프로세스 개수를 세어 calc_load_tasks 변수에 넣어주고,


calc_global_load() 가 calc_load()를 호출해서 위의 값을 보고 계산 후 avenrun[] 배열에 할당


![image](https://user-images.githubusercontent.com/85499582/233764613-78bd7c50-c198-4c11-8757-7b2aaf223fc3.png)


## Load Average 의 의미
- 계산하는 순간을 기준으로 존재하는 R,D 프로세스의 합을 바탕으로 계산
- I/O 작업 대기하는 프로세스가 많다는 의미로 볼 수도 있음
- 사실 LA값만으로는 시스템에 어떤 부하가 일어나는지 정확히 확인하기 어렵다는 의미

여기서 R,D를 좀더 생각해보면

R : Cpu Bound Process
D : I/O Bound Process 로 해석 가능

간단한 파이썬 스크립트로 프로세스를 만들어 실행시켜보면


<img width="1392" alt="image" src="https://user-images.githubusercontent.com/85499582/233765308-b8c8bda8-467c-462f-bb55-c9b43b9540b4.png">

<img width="565" alt="image" src="https://user-images.githubusercontent.com/85499582/233765337-27a98b52-1c96-4c45-9195-4e819f229947.png">


만약 각각을 실행시켜서 관측해보면

Load average는 비슷한 수준으로 나온다.

즉 cpu 를 많이먹는 프로세스와 io를 많이 먹는 프로세스에 대한 구분이 안된다는 이야기!

## vmstat으로 부하 정체 확인해보기!

### cpu bound 일때

<img width="683" alt="image" src="https://user-images.githubusercontent.com/85499582/233765480-72082fde-5425-4dd9-a49a-b065cbe47d60.png">


### io bound 일때
<img width="355" alt="image" src="https://user-images.githubusercontent.com/85499582/233765497-92e56c42-d522-4daa-8872-d7820f83caef.png">

여기서 r : R
b: D

이므로 확인가능!

## cpu 부하 상태일때와 i/o 부하상태일때 서버 응답속도 비교해보기


### cpu 부하상태일때

cpu 부하스크립트 25개 실행후 간단한 서버를 띄우고 get 요청 10번 던져서 응답속도 평균을 구해보자

<img width="1477" alt="image" src="https://user-images.githubusercontent.com/85499582/233766175-3be14337-e1e4-4267-a3ac-e2ed7e248778.png">

평균 응답속도는 0.0032

### io 부하상태일때

io 부하 스크립트 25개 실행후 간단한 서버를 띄우고 get 요청 10번 던져서 응답속도 평균 구해보자

<img width="1437" alt="image" src="https://user-images.githubusercontent.com/85499582/233766304-f257fff4-37b4-4ffd-99f8-886ff5f552e6.png">

평균 응답속도는 0.0007!

cpu부하일때가 훨씬 느리다!

위의 결과에서 top 결과를 보면 io 결과일때는 D상태로 보이며 이는 cpu 경합을 하지 않는 상황이므로 더 빠른 응답속도를 보여줄수 있는셈!


> i/o 부하일때가 응답속도가 더 빠르다!


