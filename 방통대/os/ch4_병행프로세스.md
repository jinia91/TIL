# 병행프로세스의 개요
> Concurrency, 동시성
## 병행성과 병행 프로세스
병행성 : 여러개의 프로세스 또는쓰레드가 '동시' 수행되는 시스템의 특성!
병행 프로세스 : 동시 수행되는 여러개의 프로세스 또는 쓰레드

## 병행 프로세스의 실행 형태
### 1개의 CPU : 인터리빙 형식 (RR으로 동시에 처리하는것처럼 보이는것)
### 여러개의 CPU : '병렬' 처리 형식

## 멀티 프로세서 시스템에서의 메모리구조에 따라
- 강결합 시스템(공유 메모리 구조)
  - master/slave 나 클러스터 구조
  - 최신 컴퓨터들 아키텍처(NUMA)  
- 약결합 시스템(분산 메모리 구조)
  - CPU마다 메모리를 별도로 보유하고 이를 통신으로 공유

## 프로세스간의 관계
### 독립 프로세스
- 수행 중인 다른 프로세스에 영향을 주지도 받지도 않음
- 데이터 및 상태를 다른 프로세스와 공유하지 않음
- 프로세스의 실행
  - 결정적 : 실행결과는 입력에 의해서만 결정됨
  - 재생가능 : 같은 입력에 대해 항상 동일한 실행결과

### 협력 프로세스
- 수행중인 다른 프로세스와 영향을 주고받음
- 데이터 및 상태를 다른 프로세스와 공유
- 프로세스의 실행
  - 비결정적 : 실행결과는 실행순서에 좌우
  - 재생불가능 : 같은 입력에 대해 항상 동일한 실행결과를 보장하지 못함

# 병행성 문제 : 협력프로세스인 경우 발생가능

## 상호배제

> 2개 이상의 프로세스가 동시에 임계영역을 수행하지 못하도록 하는 것

임계영역 : 2개 이상의 프로세스가 동시에 사용하면 안되는 공유자원을 액세스하는 프로그램 코드 영역


## 동기화
> 2개 이상의 프로세스에 대한 처리 순서를 결정하는 것

- 프로세스 동기화(sync)
- 상호배제도 임계영역에 대한 동기화문제로 볼 수 있음

## 통신
> 프로세스들이 데이터를 공유하기 위해 반드시 필요
- 프로세스간 통신(IPC)
- 방법
  - 하나의 변수 사용
  - 메시지를 서로 주고받음

# 세마포어
> 상호배제와 동기화 문제를 해결하기 위한 도구, 다익스트라가 제안

## 정수형 공용변수를 가짐
- 저장값 : 사용 가능한 자원의 수 또는 잠김이나 풀림의 상태(0,1)
- 상황에 맞춰 0 이상인 정수로 초기화
- 두 기본연산 P와 V에 의해서만 사용됨
  - 기본연산 : 인터럽트되지 않고 하나의 단위로 처리됨

## 연산 P
 - 검사, 감소시키려는 시도
 
 <img width="442" alt="스크린샷 2023-03-25 오후 8 31 48" src="https://user-images.githubusercontent.com/85499582/227714959-9712e1a2-6a81-4809-8753-343d3ce27d25.png">
 
- 동시성 이슈를 피하기 위해 프로세스 락같은개념

## 연산 V
- 증가


<img width="419" alt="스크린샷 2023-03-25 오후 8 32 48" src="https://user-images.githubusercontent.com/85499582/227714992-c35f525d-75ab-4bda-84fb-272f64a4a5c0.png">

## 세마포어마다 대기 큐 필요

## 상호 배제 해결
### 상호배제를 위한 일반적인 요구사항
- 한 프로세스가 임계영역 수행중 : 다른 프로세스는 임계영역에 진입해서는 안됨
- 임계영역 수행중이던 프로세스가 임계영역 벗어남 : 누군가 하나는 임계영역을 새로이 수행할 수 있어야함
- 임계영역 진입 못하고 대기하는 프로세스 : 적절한 시간 내에 임계영역 수행을 시작할 수 있어야함

### 상호배제를 위한 임계영역 주번의 코드영역

<img width="619" alt="스크린샷 2023-03-25 오후 8 35 32" src="https://user-images.githubusercontent.com/85499582/227715118-00e06ebc-e9f3-45ee-921f-dad46d11ded6.png">

<img width="321" alt="스크린샷 2023-03-25 오후 8 35 59" src="https://user-images.githubusercontent.com/85499582/227715139-50213e83-07b3-4063-9014-76bd43590ab2.png">

## 동기화도 해결가능

<img width="628" alt="image" src="https://user-images.githubusercontent.com/85499582/227715431-007ffac0-44e2-4ecc-a8e3-4f3c184f8b35.png">

- 비동기적 행위들의 순서 제어가 가능해질수 있다?
- 사실 이건 그냥 플래그 처리한는거 아닌가? 결국 공유되는 플래그 하나 보고 처리순서제어하는것일뿐인데...

# 생산자 - 소비자 문제
> 두 협력 프로세스 사이에 버퍼를 두고 생산자와 소비자의 상황을 다루기

- 생산자 : 데이터 넣기
- 버퍼 : 생산자와 소비자 사이의 저장공간
- 소비자 : 데이터 꺼내쓰기

## 조건

### 상호배제를 위한 일반적인 요구사항
- 버퍼에 여러 프로세스가 동시에 접근 불가능
- 버퍼에 데이터를 넣는 동안 데이터 꺼내기 안됨
- 버퍼에 데이터를 꺼내는 동안 데이터 넣기 불가능
== 상호배제 필요
- 버퍼 크기 유한(유한 버퍼문제)
- 버퍼가 차면 생산자 대기 필요
- 버퍼가 비면 소비자 대기 필요
== 동기화 필요

### 세마포어를 이용한 해결법
- 생산자의 코드에 데이터 넣기(버퍼접근), 소비자의 코드에 데이터사용(버퍼접근) 을 임계영역으로 정의하고 이전 진입영역에 세마포어 연산 P, 종료시 V를 사용
- 버퍼 크기가 유한한경우는?
  - 연산 P 전에 동기화를 위한 또다른 세마포어를 두고 생산자 코드에만 P, 소비자 코드가 끝날때 V를 두어 동기화를 하고 세마포어 크기를 버퍼크기 n으로 두어 사용하여 empty확인
  - 연산 P 전에 동기화를 위한 또다른 세마포어르 ㄹ두고 생산자 코드가 끝날때 V, 소비자 코드가 시작할떄 P를 두어 동기화하고 초깃값을 0으로 두어 full 확인
  
        import java.util.concurrent.Semaphore;

        class ProducerConsumer {
            static int buffer = 0;
            static final int BUFFER_SIZE = 10;
            static Semaphore mutex = new Semaphore(1);
            static Semaphore full = new Semaphore(0);
            static Semaphore empty = new Semaphore(BUFFER_SIZE);

            static class Producer implements Runnable {
                public void run() {
                    while (true) {
                        try {
                            empty.acquire();
                            mutex.acquire();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }

                        buffer++;

                        System.out.println("Producer produced item. Buffer size: " + buffer);

                        mutex.release();
                        full.release();
                    }
                }
            }

            static class Consumer implements Runnable {
                public void run() {
                    while (true) {
                        try {
                            full.acquire();
                            mutex.acquire();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }

                        buffer--;

                        System.out.println("Consumer consumed item. Buffer size: " + buffer);

                        mutex.release();
                        empty.release();
                    }
                }
            }

            public static void main(String[] args) {
                Thread producer = new Thread(new Producer());
                Thread consumer = new Thread(new Consumer());

                producer.start();
                consumer.start();
            }
        }
  

        import java.util.concurrent.Semaphore

        internal object ProducerConsumer {
            var buffer = 0
            const val BUFFER_SIZE = 10
            var mutex = Semaphore(1)
        //    var full = Semaphore(0)
        //    var empty = Semaphore(BUFFER_SIZE)

            @JvmStatic
            fun main(args: Array<String>) {
                for (i in 1 .. 10) {
                    val producer = Thread(Producer())
                    val consumer = Thread(Consumer())
                    producer.start()
                    consumer.start()

                }
            }

            internal class Producer : Runnable {
                override fun run() {
                    while (true) {
                        try {
                            mutex.acquire()
                        } catch (e: InterruptedException) {
                            Thread.currentThread().interrupt()
                        }
                        if(buffer == BUFFER_SIZE) mutex.release()
                        else {
                            buffer++
                            println("Producer produced item. Buffer size: " + buffer)
                            mutex.release()
                        }
                    }
                }
            }

            internal class Consumer : Runnable {
                override fun run() {
                    while (true) {
                        try {
                            mutex.acquire()
                        } catch (e: InterruptedException) {
                            Thread.currentThread().interrupt()
                        }
                        if(buffer == 0) mutex.release()
                        else {
                            buffer--
                            println("Consumer consumed item. Buffer size: " + buffer)
                            mutex.release()
                        }
                    }
                }
            }
        }
  
> 이렇게 해도 구현은 가능하지만, 이경우 무한루프를 돌면서 계속 cpu 연산을 하기때문에 buffer가 가득차거나 0일때 불필요한 연산이 되고, 뮤택스를 어느한쪽이 계속 잡을시 무의미한 지연이 발생
  
# 판독기-기록기 문제
> 여러 협력 프로세스 사이에 공유자원을 두고 판독기와 기록기의 상황을 다루는 문제

- 판독기 : 데이터를 읽는 프로세스
- 기록기 : 데이터를 쓰는 프로세스
  
## 문제조건
- 하나의 기록기가 공유자원에 데이터를 쓰는 중에는 다른 기록기나 판독기는 공유자원에 접근할 수 없음
- 여러 판독기는 동시에 공유자원에서 데이터를 읽을 수 있음
- 판독기한테 우선순위
- 새로운 판독기는 즉시 공유자원에 접근가능!

## 문제점
- 판독기들이 계속 공유자원에 접근한다면, 기록기의 기아상태 유발 가능

      import java.util.concurrent.Semaphore

      class ReaderWriterProblem {
          private var readCount = 0
          private val mutex = Semaphore(1)
          private val writeLock = Semaphore(1)

          internal inner class Reader : Runnable {
              override fun run() {
                  try {
                      mutex.acquire()
                      readCount++
                      if (readCount == 1) {
                          writeLock.acquire()
                      }
                      mutex.release()

                      println("Thread ${Thread.currentThread().id} is reading")
                      Thread.sleep(1000)
                      println("Thread ${Thread.currentThread().id} has finished reading")

                      mutex.acquire()
                      readCount--
                      if (readCount == 0) {
                          writeLock.release()
                      }
                      mutex.release()
                  } catch (e: InterruptedException) {
                      Thread.currentThread().interrupt()
                  }
              }
          }

          internal inner class Writer : Runnable {
              override fun run() {
                  try {
                      println("Thread ${Thread.currentThread().id} is requesting the write lock")
                      writeLock.acquire()

                      println("Thread ${Thread.currentThread().id} is writing")
                      Thread.sleep(1000)
                      println("Thread ${Thread.currentThread().id} has finished writing")

                      writeLock.release()
                  } catch (e: InterruptedException) {
                      Thread.currentThread().interrupt()
                  }
              }
          }

          fun start() {
              for (i in 1..10) {
                  val reader = Thread(Reader())
                  reader.start()
                  if (i % 3 == 0) {
                      val writer = Thread(Writer())
                      writer.start()
                  }
              }
          }
      }

      fun main() {
          val problem = ReaderWriterProblem()
          problem.start()
      }

- 이경우엔 판독기가 무한 루프일때, 기록기는 기아상태에 빠질수 있음

> 반대로 제2 판독기 - 기록기 문제는 역의 우선순위이며 이경우엔 판독기가 기아상태에 빠질 수 있음

# 프로세스간 통신(IPC)
- InterProcess Communication
- 병행 프로세스가 데이터를 서로 공유하는 방법
  - 공유메모리
  - 메시지 전달

## 메시지 전달방법
- 협력 프로세스가 메시지를 주고받음
- send(), receive()
- 소량데이터 교환에 적합

### 논리적 구조
- 통신링크 : 메시지가 지나다니는 통로
  - 통신링크 구현
    - 연결대상(노드수)
    - 연결 대상간 링크 갯수(엣지수)
    - 방향성(단, 양방향)
    - 용량(링크에 큐를 둘것인가 여부 - 동기(0) 비동기(>1))
#### 직접통신
- 직접통신은 P2P
 
- 대칭형 주소지정(커넥션 물기)
- 비대칭형 주소지정(받을때 id 받기)


#### 간접통신
- 프로세스 사이에 둔 메시징큐를 통해 메시지 전달
- 메시징큐가 수신프로세스에 소속된다면 통신링크는 단방향일수 있음
- 독립될수도있고 이때는 통신링크는 양방향
 



