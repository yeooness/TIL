n = 10

#while문
i = 0
result = 0
while i <= n:
    result += i
    i += 1
print(result)

#for문
result = 0
for i in range(n+1):
    result += i
print(result)
