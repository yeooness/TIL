#while문
n = int(input())
i = 1
result = 1
while i <= n:
    result *= i
    i += 1
print(result)

#for문
n = int(input())
i = 0
result = 1
for i in range(n):
    i += 1
    result *= i
print(result)
