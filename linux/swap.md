# swap영역
> 물리메모리가 부족할 경우를 대비해서 만들어 놓은 영역

디스크의 일부분을 메모리처럼 사용하기때문에 성능상 문제

머신에 swap이 발생할경우, 어떤 프로세스가 swap을 사용하느냐도 매우 중요한 판단기준!

## proc 디렉토리

> 프로세스 정보 등 커널 관련 정보가 저장되는 디렉터리이다.

|File/Directory|comment|
|-|-|
|/proc/[PID]/maps	|프로세스가 mapping 된 메모리 주소 공간을 보여줌. 모든 프로세스에는 각자 주소 공간이 있으며, 이 주소 공간은 가상 메모리 관리자(Virtual Memory Manager)가 제공하고 관리|
|/proc/[PID]/smaps|이 파일은 /proc/[pid]/maps에서 제공하는 정보에 더하여, 각 메모리 매핑에 대한 추가적인 세부 정보를 제공|
|/proc/[PID]/cmdline	|프로세스 인수(argv) 전체를 포함. Command Line에서 넘어온 argumnet를 포함하여 프로세스가 질생된 방식을 정확하고 신속하게 파악하는 수단으로 사용|
|/proc/[PID]/coredump_filter	|메모리 유형의 비트마스크를 포함하며 프로세스의 어떤 메모리 세그먼트를 덤프시킬 것인지 설정 |
|/proc/[PID]/cwd/	|프로세스가 사용중인 디렉토리나 파일|
|/proc/[PID]/environ	|프로세스의 현재 환경을 저장. 프로세스 map에서 가장 아랫부분, 즉 커널이 프로세스 환경 정보를 저장하는 메모리 위치를 직접 가리키는 링크이다. 프로그램 실행 중 환경 변수 설정을 알고 싶을 때 이 파일을 확인하면된다.|
|/proc/[PID]/exe	|	실행중인 프로그램 이름|
|/proc/[PID]/fd, /proc/[PID]/fdinfo|프로세스가 사용중인 File Descriptor 링크와 정보 저장|
|/proc/[PID]/limits	|	프로세스에 적용된 resource 제한 사항|
|/proc/[PID]/loginuid|해당 프로세스를 실행하는 login UID|
|/proc/[PID]/mem|프로세스가 사용중인 메모리 상태|
|/proc/uptime|시스템 가동 시간에 대한 정보를 기록한다.|
|/proc/meminfo|물리적 메모리 및 스왑 메모리 정보가 들어 있는 파일이다.|
|/proc/cmdline|부팅 시에 실행되는 커널 관련 옵션에 대한 정보를 담고 있다.|
|/proc/loadavg|최근 1분, 5분. 15분 동안의 평균 부하율을 기록하는 파일이다.|

- 여기서 smap으로 찾아가 어능여역이 swap에 해당하는지 확인 가능!
- status나 smem 를 통해서도 확인가능
