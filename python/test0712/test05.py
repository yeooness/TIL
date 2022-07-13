# 1. 문제 제공 
numbers = [3, 10, 20]

# 2.값 초기화 
result = 0
count = 0 

# 3. 반복 
for number in numbers:
    result +=  number 
    count += 1 

    print(int(result/count))
