# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

for dan in range(2, 10):    # 2~9단 
    print(f'-- {dan}단 --')  # 몇단인지 표시
    for i in range(1, 10):  # 1~9
        print(f'{dan} x {i} = {dan * i}')




