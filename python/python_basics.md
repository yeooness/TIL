# ✏️ Python 기초

> 1. 기초문법
>
> 2. 파이썬 기본 자료형 
>
> 3. 컨테이너 



## 1. 기초문법

- space sensitive

  - 문장을 구분할때, 들여쓰기를 사용 
  - 들여쓰기를 할 때는 4칸 혹은 1탭을 입력 

- 변수(variable)란?

  - 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름 

  - 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것 

    → 파이썬은 객체지향 언어이며, 모든것이 객체로 구현되어 있음 

  - 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에, 즉 참조하는 객체가 바뀔 수 있기 때문에 '변수'라고 불림

  - 변수는 할당 연산자(=)를 통해 값을 할당 

    ```python
    # 실습문제
    실습 문제 x = 10, y = 20 일 때, 각각 값을 바꿔서 저장하는 코드를 작성하시오
    
    # 풀이: 임시적인 변수가 필요하다
    tmp = x
    x = y
    y = tmp
    print(x, y)
    # 다른 풀이: pythonic!
    y, x = x, y
    print(x, y)
    ```

- 식별자
  - 파이썬 객체를 식별하는데 사용하는 이름
  - 규칙
    - 식별자의 이름은 영문 알파벳, 언더스코어, 숫자로 구성
    - 첫 글자에 숫자가 올 수 없음
    - 길이제한이 없고, 대소문자를 구별
    - 다음의 키워드는 예약어로 사용할 수 없음 (pdf 보고 정리)

- 사용자 입력

  - input([prompt])

    ```python
    name = input('이름을 입력해주세요')
    print(name)
    ```

- 주석
  - 한 줄 주석 주석으로 처리될 내용 앞에 '#' 을 입력



## 2. 자료형

- 불린(boolean)형

  - True / false 

- 수치형

  - int , float 

- 문자열

  - string 

    ```python
    # %-formating
     name = 'Kim' score = 4.5
     print('Hello, %s' % name) 
     print('내 성적은 %d' % score)  
     print('내 성적은 %f' % score)
    # Hello, Kim
    # 내 성적은 4
    # 내 성적은 4.500000
    
    # f-string
     name = 'Kim'
     score = 4.5
     print(f'Hello, {name}! 성적은 {score}') # Hello, Kim! 성적은 4.5
    
     pi = 3.141592
     print(f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}') # '원주  율은 3.14. 반지름이 2일때 원의 넓이는 12.566368'
    ```

  - 인덱싱

    Ex) abcdefghi

    s[1] ⇢ 'b'

  - 슬라이싱 

    Ex) s[2:5] ⇢ 2 이상 5 미만 ('cde')

    ​      s[2:5:2] ⇢ 2 이상 5 미만 범위내에서 두칸씩 ('ce')

    ​      s[5:2:-1] ⇢'fed'

    ​      s[:3] ⇢ 'abc'

    ​      s[5:] ⇢fghi

  - 기타 

    ```python
    # 결합
    'hello, ' + 'python!' # 'hello, python!'
    
    # 반복
    'hi!' * 3
    # 'hi!hi!hi!'
    
    # 포함
    'a' in 'apple' # True
    'app' in 'apple' # True
    'b' in 'apple'
    # False
    ```

- none

  

## 3. 컨테이너

- 시퀀스

  - 문자열 : 문자들의 나열 

  - 리스트 : 변경 가능한 값들의 나열 

    ```python
    # 값 접근
    a = [1, 2, 3] print(a[0]) #1
    
    # 값 변경
    a[0] = '1' print(a)
    # ['1', 2, 3]
    
    # 값 추가 
     even_numbers = [2, 4, 6, 8]
     even_numbers.append(10) 
     even_numbers
     # => [2, 4, 6, 8, 10]
    
    # 값 삭제
     even_numbers = [2, 4, 6, 8]
     even_numbers.pop(0)
     even_numbers
     # => [4, 6, 8]
    
    ex) boxes = ['apple', 'banana']
        len(boxes) #2
        boxes[1] #'banana'
        boxes[1][0] #'b'
    ```

  - 튜플 : 변경 불가능한 값들의 나열

  - 레인지 : 숫자의 나열

    ```python
    # 0부터 특정 숫자까지
      list(range(3))
      # [0, 1, 2]
    
    # 숫자의 범위
     list(range(1, 5)) 
     # [1, 2, 3, 4]
    
    # step 활용 
     list(range(1, 5, 2)) 
      # [1, 3]
      
    # 역순
     list(range(6,1,-1))
      # [6,5,4,3,2] 
     list(range(6,1,1))
      # []
    ```

- 컬렉션/비시퀀스

  - 세트 : 유일한 값들의 모임, 순서가 없고 중복된 값이 없음, 변경 가능, 반복 가능 

    ```python
    # 세트 생성 
    {1, 2, 3, 1, 2}
    # {1, 2, 3}
    type({1, 2, 3}) 
    # <class 'set'> 
    blank_set = set()
    
    # 세트 추가/삭제 
     numbers = {1, 2, 3}
     numbers.add(5) 
     numbers
     # => {1, 2, 3, 5} 
     numbers.add(1) 
     numbers
     # => {1, 2, 3, 5}
     numbers = {1, 2, 3} 
     numbers.remove(1)
     numbers
     # => {2, 3} 
     numbers.remove(5)
     # Traceback (most recent call last): # File "<stdin>", line 1, in <module> #KeyError: 5 
      
    # 세트 활용 
     my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산’]
    len(set(my_list))
    #4
    set(my_list)
    # {'광주', '대전', '부산', '서울'}
    ```

    

  - 딕셔너리 : 키-값들의 모임

    ```python
    # 딕셔너리 접근 
     movie = {
          'title': '설국열차',
          'genres': ['SF', '액션', '드라마'], 
          'open_date': '2013-08-01', 
          'time': 126,
          'adult': False,
    }
     movie['genres']
     # ['SF', '액션', '드라마']
     movie['actors’]
     Traceback (most recent call last): File "<stdin>", line 1, in  <module> KeyError: 'actors'
           
    # 딕셔너리 키-값 추가 및 변경 
      students = {'홍길동': 100, '김철수': 90} 
      students['홍길동'] = 80
      # {'홍길동': 80, '김철수': 90}
      students['박영희'] = 95
      # {'홍길동': 80, '김철수': 90, '박영희': 95}
           
    # 딕셔너리 키-값 삭제 
      students = {'홍길동' : 30, '김철수' : 25}
      students.pop('홍길동')
      students
      # {'김철수' : 25}
    ```

    



