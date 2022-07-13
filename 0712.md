## python 제어문

> 1. 조건문
> 2. 반복문 



## 1. 조건문

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용. 

  ```python
  if <expression> : 
      # run this code block (네칸 띄어쓰기) 
  else : 
      # run this code block
  ```

  - 실습문제

    ```python
    # 조건문을 통해 변수 num 의 홀수 / 짝수 여부 출력
      num = int(input())
      if num % 2 == 1 :  
          print("홀수")
      else : 
          print("짝수")
    ```

 - 복수 조건문 

   ```python
   if <expression> : 
   	# code block 
   elif <expression> : 
   	# code block 
   elif <expression> : 
   	# code block 
   # 조건문에서 else 는 생략 가능   
   else <expression> : 
     # code block 
   ```

   - 실습문제 

     ```python
     # 미세먼지 농도 
     dust = int(input())
     if dust > 150  : 
     	print('매우나쁨')
     elif dust > 80 :  
       print('나쁨')
     elif dust > 30 : 
       print('보통')
     else : 
       print ('좋음')
     print('미세먼지 확인 완료')
     ```

- 중첩 조건문 

  ```python
  dust = int(input())
  if dust > 150  : 
    if dust > 300 :
       print('실외활동을 자제하세요.') 
  	print('매우나쁨')
  elif dust > 80 :  
    print('나쁨')
  elif dust > 30 : 
    print('보통')
  else : 
    if dust < 0 : 
      print('음수 값입니다.')
    else : 
      print ('좋음')
  print('미세먼지 확인 완료')
  ```

- 조건 표현식 

  ```python
  # 절대값 작성 코드 (조건표현식 코드)
   value = num if num >= 0 else -num
         참일경우   <expression>   거짓일경우
      
  # 조건문 코드 
  # 1. 양수면 그대로 
    if num >= 0 : 
      value = num 
  # 2. 음수면 - 붙여서 
    else : 
      value = -num
    print(num,value)  
  ```



## 2. 반복문

- While문 

  - 조건식이 참인 경우 반복적으로 코드를 실행 

    - 조건이 참인 경우 들여쓰기 되어 있는 코드 불록이 실행됨
    - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
    - while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요 

  - 실습문제

    ```python
    # 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드 작성
     
    # 값 초기화 
    n = 0
    total = 0
    user_input = int(input())
    
    #1
    while n <= user_input : 
      total += n
      n += 1 
     print(total) 
    
    #2
    while n < user_input:
        n += 1 
        total += n
    print(total)
    ```

- for 문 

  - 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체 요소를 모두 순회함 

  - 처음부터 끝까지 모두 순회하므로 별도의 종료조건 필요하지 않음 

    ```python
    # 문자열 순회 
    # 사용자가 입력한 문자를 한 글자씩 세로로 출력 
    chars = input() # hi 
    for char in chars : 
      print(char) 
    
    # 사용자가 입력한 문자를 range를 활용하여 한 글자씩 출력
    chars = input() #hi 
    for idx in range(len(chars)) : 
      print(chars[idx])
      
    # enumerate 순회
     # 인덱스와 객체를 쌍으로 담은 열거형(enumerate)객체 반환 
    members = ['민수', '영희','제니']
    for i in range(len(members)):
      print(f'{i}{members[i]}')
    for i, member in enumerate(members) : 
      print(i, member)
      
    # 딕셔너리 순회
    grades = {'john' : 80, 'eric' : 90}
    for name in grades : 
      print(name) 
      #john
      #eric 
    grades = {'john' : 80, 'eric' : 90} 
    for name in grades : 
      print(name, grades[name]) 
      #john 80
      #eric 90 
    ```

- 반복문 제어 

  - break 

    ```python
    # 1. 
    n=0
    while True:
        if n == 3:
            break
    print(n) n += 1
     #0 1 2 
    
    #2. 
    for i in range(10):
        if i > 1:
    print('0과 1만 필요해!')
    break
    print(i)
     #0 1 0과 1만 필요해!
    ```

  - continue

    conitnue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행 

    ````python
    for i in range(6): 
      if i % 2 == 0:
    continue
    print(i)
    # 1 3 5 
    ````

  - for-else 

    ```python
    for char in 'apple' : 
        if char == 'b':
           print('b!')
           break 
    else:
           print('b가 없습니다.')
    ```

    























