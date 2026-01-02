## "파이썬은 모든 것이 객체다(Everything is an object in Python)”
<details>
<summary>print</summary>
  
```
#구분자 지정: sep
print('A1', 'B1', sep=',') -> A1, B1

#줄바꿈X
print('aa', end=' ')
print('bb')
-> aa bb

#리스트 출력
li = ['A1', 'B1']

print(*li) -> A1 B1
print(' '.join(li)) -> A1,B1

#f-string
idx = 1
fruit = "Apple"

print('{}: {}'.format(idx + 1, fruit)) 
print(f'{idx + 1}: {fruit}') -> 2: Apple
```
</details>


<details>
<summary>input</summary>

- 원하는 형태로 input 받기
    
```
#[1,2,3,4,5]를 deque에 넣기

import sys 
input = sys.stdin.readline # 버퍼를 사용하여 한 번에 읽어오기 때문에 빠르게 처리 가능 
from collections import deque

deque(input().rstrip()[1:-1].split(","))
```
    
- 공백 없는 input을 하나씩 리스트에 저장하고 싶을 때

```python
# input -> 10101111
# output -> [1, 0, 1, 0, 1, 1, 1, 1]

import sys 
input = sys.stdin.readline

list(map(int, list(input().rstrip())))

-> int 변환이나 split을 사용할 때는 공백 제거 로직을 추가하지 않아도 됨
```

</details>


<details>
<summary>자료형</summary>

- 리스트 : [1, 2, 3] → 수정O, 순서O, 중복O
    - 선언
    
    ```python
    a = list()
    a = []
    ```
    
    - 추가
    
    ```python
    #맨 뒤에 아이템 추가
    list_name.append(a)
    
    #특정 위치에 아이템 추가
    list_name.insert(3, 5) -> 3번째 인덱스에 5를 삽입
    ```
    
    - 삭제
    
    ```python
    a = [10, 20, 30]
    
    #인덱스로 삭제
    del a[0]
    #값으로 삭제
    a.remove(10)
    #리턴 후 삭제
    a.pop(0)
    ```
    
- 딕셔너리 : {”a”:“A”, “b”:“B”, “c”:”C”} → 수정O, 순서O(OrderedDict 사용해야 함), key는 중복X, value는 중복O
    - 선언
    
    ```python
    a = dict()
    a = {}
    ```
    
    - 추가
    
    ```python
    a['key_name'] = 'value_name'
    ```
    
    - 키, 값 조회
    
    ```python
    for k, v in a.items():
            print(k, v)
    ```
    
    - 삭제
    
    ```python
    del a['key_name']
    ```
    
    - Counter : 빈도수 계산
    
    ```python
    from collections import Counter
    
    a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
    b = Counter(a)
    b -> Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
    
    #가장 높은 빈도수를 가지는 요소 
    c = b.most_common(2) -> 2개 출력
    c -> [(5, 3), (6, 2)]
    ```
    
    - OrderedDict : 순서 지정
    
    ```python
    from collections import OrderedDict
    OrderedDict(a) 
    ```
    
- 튜플 : (1, 2, 3) → 수정X, 순서O, 중복O
    
    → 수정이 안되는 특정 때문에 요소를 변경하려면 리스트로 변환한 후 변경하고 다시 튜플로 변경 해야함
    
- 집합 set : {”a”, “b”, “c”} → 수정O, 순서X, 중복X
    
    ```python
    s = {1, 2, 3}
    추가(싱글 요소) - add
    추가(열거형 자료) - update
    제거(싱글 요소) - remove : 제거 대상 없으면 에러 발생
                                discard : 제거 대상 없어도 에러 발생X

    * 주의: 선언과 동시에 초기화 할 때는 반드시 리스트로 감싸줘야 한다. (예) set([i for i in range(1, 11)])) 그렇지 않으면 문자열을 쪼개서 하나의 요소로 인식하려고 함.
    ```
    
    - any
    
    ```python
    vset = {1, 2, 3, 3} -> {1, 2, 3}
    ex = {3, 4, 5}
    # vset에 ex에 있는 값 하나라도 있으면 True
    if any(vset and ex):
        print(True)
    ```
    
- int, str
    - 문자열을 숫자로 변환하여 형식에 맞게 다시 문자열로 변환
    
    ```python
    original_strings = ['0', '90', '123', '20']
    
    # 각 문자열을 숫자로 변환하여 형식에 맞게 다시 문자열로 변환
    -> 4자리수에 맞춰 앞을 0으로 채우기
    transformed_strings = ['{:04d}'.format(int(s)) for s in original_strings]
    
    -> 4자리수에 맞춰 뒤를 0으로 채우기
    transformed_strings = ['{:<04d}'.format(int(s)) for s in original_strings]
    
    print(transformed_strings) -> ['0000', '0090', '0123', '0020']
    ```


</details>
<details>
<summary>나눗셈 연산</summary>
    
```
#몫
5 / 3 -> 1.6666..
5 // 3 -> 1

#나머지
5 % 3 -> 2

#몫과 나머지
divmod(5, 3) -> (1, 2)
```

</details>


<details>
<summary>리스트 복제</summary> 
- 리스트 객체 생성자인 list() 함수 사용

```python
a = [1, 2, 3]
b = list(a)		 
b[0] = 100
print(a, b)
=> [1, 2, 3] [100, 2, 3]
```

- 리스트의 copy() 내장 함수 사용

```python
b = a.copy()		
b[0] = 100
print(a, b)
=> [1, 2, 3] [100, 2, 3]
```

→ 2차원 이상일 경우 deepcopy사용

```python
import copy
a = [1, [10, [100, 200]]]
b = copy.deepcopy(a)		 
b[1][1][0] = -1
print(a, b)
=> [1, [10, [100, 200]]] [1, [10, [-3, 200]]]
```

- 리스트의 슬라이싱 사용

```python
b = a[:]	
b[0] = 100
print(a, b)
=> [1, 2, 3] [100, 2, 3]
```

</details>


<details>
<summary>특정 요소의 인덱스 찾기</summary>   

```
arr = [10, 20, 30]
print(arr.index(10)) -> 0
```

</details>


<details>    
<summary>리스트 컴프리헨션</summary>
    
```
list(map(lambda x: x + 10, [1, 2, 3])) -> [11, 12, 13]
```

```
#리스트 컴프리헨션X
a = []
for i in range(1, 11):
        if n % 2 == 1:
                a.append(n * 2)

#리스트 컴프리헨션O
[n * 2 for i in range(1, 11) if n % 2 == 1]
```

```p
#리스트 컴프리헨션X
a = {}
for key, value in original.items():
        a[key] = value

#리스트 컴프리헨션O
a = {key : value for key, value in original.items()}
```

</details>


<details>
<summary>enumerate</summary>   
    
```
a = [1, 2, 3, 2, 45]

enumerate(a)
-> <enumerate object at 0x000002C7F4448630>

list(enumerate(a))
-> [(0,1), (1,2), (2,3), (3,2), (4,45)]
```

```
a = ['a1', 'a2', 'a3']

for i, v in enumerate(a):
    print(i, v)
-> 0 a1
     1 a2
     2 a3
```

</details>


<details>
<summary>join</summary>
- 문자열을 합치는 함수

```python
words = ["Hello", "World", "!"]
combined_string = " ".join(words) -> Hello World !
```

```python
words = ["Hello", "World", "!"]
combined_string = ".".join(words) -> Hello.World.!
```

</details>


<details>
<summary>람다함수를 활용한 sort</summary>
- 2차원 리스트 정렬

```
# 첫 번째 요소를 기준으로 정렬
vlist = [[80,20],[50,40],[30,10]]
sorted_vlist = sorted(vlist, key=lambda x: x[1])
```

```
# 첫 번째 요소를 기준으로 정렬 후 두 번째 요소를 기준으로 정렬
vlist = [[80,20],[50,40],[30,10]]
sorted_vlist = sorted(vlist, key=lambda x: (x[0], x[1]))
```

```
# 첫 번째 요소를 내림차순 정렬 후 두 번째 요소를 오름차순 정렬
vlist = [[80,20],[50,40],[30,10]]
sorted_vlist = sorted(vlist, key=lambda x: (-x[0], x[1]))
```

</details>


<details>
<summary>람다함수를 활용한 리스트 조작</summary>

```
vlist = [1, 2, 3]

result = list(map(lambda x: x-1, vlist))
```

- 2차원 리스트 문자열

```
list_data = [['1212345'], ['1212356'], ['33445']]
sliced_list = list(map(lambda x: x[0][:3], list_data)) 
                            -> [['121'], ['121'], ['334']]
```

</details>


<details>
<summary>itertools → 순열, 조합</summary>
- 순열

```
from itertools import permutations

vlist = [10, 20, 30] # 2차원 리스트도 가능
permut = list(permutations(vlist, len(vlist)))
print(permut) -> [(10, 20, 30), (10, 30, 20), (20, 10, 30), (20, 30, 10), (30, 10, 20), (30, 20, 10)]
```

→ permutations를 list()로 감싸줘야 하는 이유는?

permutations는 iterable객체로 반복 가능한 객체이다. 즉, 반복문을 사용하여 그 안에 있는 순열들을 하나씩 가져올 수 있으나 명시적으로 iterable한 형태(열거형 자료형)로 변환하지 않으면 순열을 직접적으로 확인할 수는 없다.

- 조합

```
from itertools import combinations

vlist = [10, 20, 30]
combi = list(combinations(vlist, len(vlist)))
print(combi)
```

</details>


<details>
<summary>collections</summary>
    
- deque→ Queue 구현
```
from collections import deque

que = deque([2, 3, 4])
# 뒤에 추가
que.append(5) -> [2, 3, 4, 5]
# 앞에 추가
que.appendleft(1) -> [1, 2, 3, 4, 5]
# 맨 뒤에 값 꺼내기
que.popleft() -> 5
# 맨 앞에 값 꺼내기
que.pop() -> 1

*list에서 사용하는 연산이 가능하다.(append, pop, insert...)
```

→ 리스트처럼 인덱스로 접근 가능
    
- Counter   
```
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'blue', 'green', 'red'])

print(counter['blue']) -> 2
print(counter['red']) -> 3
print(dict(counter)) -> {'red': 3, 'blue': 2, 'green': 1}

words = 'AABB'
n_words = Counter(words) -> {'A':2, 'B':2}
```

- Counter로 인해 dict으로 묶인 요소들을 key, value 형태로 접근하려면?

```
for k, v in 
```
    
- defaultdict
```
from collections import defaultdict

# 리스트를 기본값으로 가지는 defaultdict 생성
d = defaultdict(list)
d['example'].append(1)
print(d['example']) => 1

# int를 기본값으로 가지는 defaultdict 생성
d = defaultdict(int)
d['count'] += 1
print(d['count']) => 1

# 사용자 정의 함수를 기본값으로 가지는 defaultdict 생성
def default_value():
        return 'default'
d = defaultdict(int)
print(d['key']) => 'default'
```
    
- OrderedDict: Python 3.7 이전 버전에서 딕셔너리의 순서를 기억하기 위함
```
from collections import OrderedDict

d = OrderedDict()
d['b'] = 2
d['a'] = 1
d['c'] = 3

print(d) -> OrderedDict([('b', 2), ('a', 1), ('c', 3)])
```

</details>


<details>
<summary>startswith, endswith</summary>
    
- startswith(접두사): 지정하는 특정 문자로 시작하는지

```
str = 'kang minji'
result = str.startswitch('kang')
print(result) -> True
```

- endswith(접미사): 지정하는 특정 문자로 끝나는지

```
str = 'hojun ddong'
result = str.endswitch('ddong')
print(result) -> True
```

</details>


<details>
<summary>시간 복잡도, 공간 복잡도</summary>
    
- 시간 복잡도: 연산 횟수
  - 1초 2,000만 개(20*10^7) ~ 1억 개(10^8)
  - O(N): => 단순 반복문, input 
  - O(logN): 10억 개를 30번 만에 처리 가능(log10^9 = log2^30) => 이분탐색
  - O(NlogN): 몇 십만 개라면 처리 가능(log10^6 = 20 -> 20*10^6 = 2,000만 번)  => 정렬, 힙
  - O(N^2): 10,000개만 되어도 (10^4)^2 = 10^8 = 1억 번으로 위험 => 2중 반복, 플루이드 워셜
  - O(2^N): 20~25개 미만이 안전 (2^20 = 10^6, 2^30 = 10^9)
 
  * 주의사항 *
  - str은 int보다 2~3느리다. int형 변수를 사용한다면 str보다 int를 사용하자
  - 반복문이나 조건문 내부에 리스트의 요소를 참조하는 로직이 반복 된다면 지역변수로 따로 선언하는 것이 더 빠르고 안전하다

- 공간 복잡도: 변수가 차지하는 크기
  - 보통 리스트 때문에 발생 => 2차원 리스트 지양, 입력 받을 때 너무 많은 요소를 한 번에 리스트로 받으려 하면 메모리 에러 발생할 수 있음
  - set, dict 3~4배 소모, 깊은 재귀 주의 
  - int 요소 1개: 4~8byte
  - 1MB = 약 25만 개 정수, 128MB = 약 1,500만 개~3,000만 개 정수

</details>

