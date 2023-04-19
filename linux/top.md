<img width="816" alt="스크린샷 2023-04-19 오전 1 30 05" src="https://user-images.githubusercontent.com/85499582/232843455-88140d9e-d29b-48c7-9cc0-44d3737e8e69.png">

# 대쉬 항목
- PR : 프로세스 우선순위
- NI : PR 보정값
- VIRT : task가 사용하고있는 가상 메모리의 전체용량
- RES : 현재 사용중인 물리메모리 양
- SHR : 공유 메모리양 다수 프로세스가 함께 사용하는 라이브러리를 공유메모리에 올려 사용!
- S : 상태

## 메모리

- 가상메모리 할당?

커널로부터 프로세스가 사용을 예약받은 메모리양.
malloc() 같은 시스템콜로 자신이 필요로 하는 메모리의 영역을 할당해 줄것을 요청 후 가상메모리를 할당, 물리메모리가 아니다

- 이러한 동작방식을 Memory Commit이라고 함

> 커널 파라미터내의 vm.overcommit_memory 파라미터를 통해 동작 방식 정의도 가능

이후 프로세스가 할당받은 메모리 영역에 실제로 쓰기 작업을 하면, Page Fault 가 발생! -> 커널은 실제 물리메모리에 프로세스의 가상 메모리를 매핑, Page Table 이라는 커널 전역변수로 관리
-> res

### 가상 메모리 할당 실습

#### 1. 가상메모리 할당


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h> // Added to include the sleep() function.

#define MEGABYTE 1024*1024

    int main() {
      void *myblock = NULL; // Changed 'null' to 'NULL'
      int count = 0;

      while (1) {
        myblock = (void *) malloc(MEGABYTE); // Removed the extra space between 'my' and 'block'
        if (!myblock) {
          printf("ERROR!\n"); // Added a newline character for better output formatting
          break;
        }
        printf("currently allocating %d MB\n", (++count)); // Removed * MEGABYTE as count is already in MB
        // memset(myblock, 1, MEGABYTE);
        sleep(1);
      }
      exit(0);
    }
    
    
<img width="1501" alt="image" src="https://user-images.githubusercontent.com/85499582/232852096-b6c76d13-d744-4f11-9ea4-e125cbc14ee2.png">

 계속 가상메모리 할당만 하고 있으므로 프로세스에 할당된 virt는 올라가지만, 실제 res는 변화없다.
 
 
    
#### 2. 메모리를 받은순간에 사용하기(memset())

   int main() {
      void *myblock = NULL; // Changed 'null' to 'NULL'
      int count = 0;

      while (1) {
        myblock = (void *) malloc(MEGABYTE); // Removed the extra space between 'my' and 'block'
        if (!myblock) {
          printf("ERROR!\n"); // Added a newline character for better output formatting
          break;
        }
        printf("currently allocating %d MB\n", (++count)); // Removed * MEGABYTE as count is already in MB
        memset(myblock, 1, MEGABYTE);
        sleep(1);
      }
      exit(0);
    }
    
    
    
<img width="1428" alt="image" src="https://user-images.githubusercontent.com/85499582/232853027-f4dc8b34-9c65-4457-9f82-ef7320e3f49f.png">

res도 상승중!

만약 물리메모리를 계속 할당받는다면, 물리메모리에 더이상 할당이 불가능할경우 swap이 일어나거나, oom으로 프로세스를 죽이는 등의 방법으로 메모리 확보하게 될것.

#### 그러면 virt는 무제한으로 할당가능할까?

memory commit : 프로세스가 커널에 필요한 만큼의 메모리를 요청하면 커널은 프로세스에 사용가능한 메모리 영역을 주고  실제로 할당은 하지 않지만, 해당 영역을 프로세스에 주었다는 것을 저장해둔다. 이 일련의 과정을 메모리 커밋이라고 부름

실제 할당을 즉시 하지 않고, 커밋만 하고 지연하는 이유는?

- fork()와 같은 새로운 프로세스를 만들기 위한 콜을 처리해야 하기 때문
- fork() 시스템 콜을 사용하면 커널은 실행중인 프로세스와 똑같은 프로세스를 하나 더 만들고, exec() 시스템 콜을 통해 다른 프로세스로 변함. 이 때 확보한 메모리가 쓸모 없어질 수 있음
- COW(Copy-On-Write) 기법을 통해 복사된 메모리 영역에 실제 쓰기 작업이 발생한 후 실질적인 메모리 할당을 진행


### vm.overcommit_memory

sysctl.conf 에 있는 vm.overcommit_memory 값은 커밋을 어떻게 제어할 것인지에 대한 커널 설정값

0 – 적당히 휴리스틱하게 처리
1 – 항상 허용
2 – vm.overcommit_memory_ratio 에 적용된 범위까지만 허용

레디스 사용시 메모리단을 볼일이 많기때문에 실무적으로 튜닝할 일이 존재할수도 있음.

1로 설정시엔 모든 요청에 일단 커밋허용이 되므로, 가용메모리보다 훨씬 큰 메모리 요청시 swap이 일어날수 있다.





## 프로세스 상태보기

S - Process Status
- D : Disk Slepping 디스크 혹은 네트워크 I/O 대기, wait queue
- R : 실행중인 프로세스
- S : sleeping 상태
- T : 시스템콜을 추적하고 있는 상태
- Z : 부모 프로세스가 죽은 자식 프로세스


좀비 프로세스는 시스템 리소스 사용 x 스케줄러에 선택되지 않음, PID 고갈 문제가 발생할 수는 있다.

