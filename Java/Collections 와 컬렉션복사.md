# Collections
## intro
얼마전 회사 코드에서 셔플을 위해 Collections.shuffle() 을 사용할 일이 있었는데 이참에 Collections 클래스에 대해 정리해보고싶은 마음이 들었다.

> Collections 클래스는  Collection Framework를 조작하기 위해 정적메서드를 모아놓은 유틸 클래스다.


<img width="729" alt="스크린샷 2022-08-25 오전 12 14 39" src="https://user-images.githubusercontent.com/85499582/186456161-df8473dc-795f-4643-941a-986e256a444b.png">

- 유틸 패키지에 위치

## 주요 메서드와 코멘트

### sort(List list), sort(List list, Comparator)

- ps에서 자주쓰는 정렬메서드로 내부적으로 merge-sort로 이루어짐
- 첨언으로 primitive 타입을 사용하는 Arrays.sort() 배열 정렬의경우 내부 알고리즘으로 퀵정렬을 사용하는데 퀵정렬은 시간복잡도가 일반적으론 O(nlogN)이나 최대 O(n^2)까지 증대될수 있으므로 merge-sort에 비해 최악의 경우 정렬이 느려짐

### binarySearch(List list, T key),  indexedBinarySearch(List<? extends Comparable<? super T>> list, T key) 

- 이진탐색으로 인덱스 찾기
- List.indexOf() 메서드도 존재하는데 정렬된 리스트에 한에서 이진탐색은 시간복잡도 O(nlogN)이므로 선형탐색인 indexOf()의 시간복잡도 O(N)에 비해 더 빠르다

### shuffle(List list), shuffle(List list, Random seed)
<img width="578" alt="스크린샷 2022-08-25 오전 12 39 45" src="https://user-images.githubusercontent.com/85499582/186461845-f0ec6aa7-5801-4c84-9899-ba4f52fc09cf.png">

- 리스트를 셔플링
- 난수 시드를 동일하게 넣으면 셔플링도 동일하게 됨

## 컬렉션 생성과 복사관련 `ImmutableCollections` vs `unmodifiableCollection`에 대해

<img width="886" alt="스크린샷 2022-08-25 오전 12 44 24" src="https://user-images.githubusercontent.com/85499582/186462801-6af59885-4f2e-4be2-8812-092a2dad5dd4.png">

- `unmodifiableCollection`은 컬렉션프레임워크 차원에서 컬렉션이 수정불가가 보장되야하는 상황에 사용되는 클래스로 api로 정의된 변경 메서드들을 호출시 예외를 터뜨리게 오버라이딩 되어있음
- 하지만 unmodifiableCollection이 불변객체임을 보장하는것은 아님
- 그 이유는 Collections.unmodifiableList(List list) 를 통해 `수정불가 리스트`를 생성할때, 이 수정불가 리스트는 원본 리스트를 참조하는 일종의 래퍼 객체로, 사실상 얕은 복사를함  
- 따라서 `수정불가 리스트`는 수정이 불가능하나, 원본 리스트는 수정이 가능하고, 원본 리스트를 수정하면 `수정불가 리스트`도 변경이 일어남!

- 참고로 `List.of()`로 생성시 불변 객체 리스트로 생성

<img width="634" alt="스크린샷 2022-08-25 오전 12 47 43" src="https://user-images.githubusercontent.com/85499582/186463529-9e748b08-6d1d-45f6-be2c-993490c8943c.png">


### 불변객체로서 List.copyOf() 와 수정불가 객체로서 Collections.unmodifiableList()
<img width="780" alt="스크린샷 2022-08-25 오전 1 12 11" src="https://user-images.githubusercontent.com/85499582/186469188-3deb6080-0997-45d8-ab21-3c98d3f3b93e.png">
- copyOf로 복사시엔 참조값이 다 끊기기 때문에 원본 리스트와는 별개의 리스트가 되나, Collections.unmodifiableList()는 순수하게 래핑만 하기때문에 원본수정에 영향받는다
