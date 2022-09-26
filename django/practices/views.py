from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    # name = request.GET.get('ball')
    # context = {
    #     'name':name,
    # }

    return render(request, "pong.html", {"name": request.GET.get("ball")})


# 홀짝
def print_number(request, number):
    result = []
    if number % 2 == 0:
        result.append("짝수")
    else:
        result.append("홀수")

    context = {
        # "템플릿 변수 이름" : 값
        "number": number,
        "result": result,
    }
    return render(request, "number.html", context)


# 계산기
def cal(request, num1, num2):
    context = {
        "plus": f"{num1} + {num2} = {num1 + num2}",
        "minus": f"{num1} - {num2} = {num1 - num2}",
        "multi": f"{num1} * {num2} = {num1 * num2}",
        "divide": f"{num1} // {num2} = {num1 // num2}",
    }
    return render(request, "cal.html", context)


# 전생
def past(request):

    return render(request, "past-life.html")


def result(request):
    name = request.GET.get("q")
    result = [
        ("공주", "https://dimg.donga.com/wps/NEWS/IMAGE/2009/11/28/24435812.1.jpg"),
        (
            "왕자",
            "https://post-phinf.pstatic.net/MjAxOTEwMDdfMjU2/MDAxNTcwNDUzODU0MTk5.QmP2TD_SM-NVtNgMrUkYnpfie5MKHAO2Mypm76JqFqYg.v5YBrBvhBEL_l58oJ5x65yPwbaRitXcPIBr6hksQhoYg.PNG/디즈니.png?type=w1200",
        ),
        (
            "꽃",
            "https://mblogthumb-phinf.pstatic.net/MjAyMDAzMTNfMTUz/MDAxNTg0MDc0OTI5MTMz.uJm-kdKZTOlxJZis7Uf6APQ1gEv9a8YmgSPMXXjy63Ig.SiCOkm1obZ0VUhvTqVKvFsXlGJum8F5AizK6_iFVeEEg.JPEG.julyhoho/SE-5d32444c-a0ec-4dd8-81ea-9d983f2b3628.jpg?type=w800",
        ),
        (
            "강아지",
            "http://image.dongascience.com/Photo/2022/06/6982fdc1054c503af88bdefeeb7c8fa8.jpg",
        ),
        ("나무", "https://t1.daumcdn.net/cfile/tistory/994141415EE3015401"),
        ("하늘", "http://www.chemicalnews.co.kr/news/photo/201908/822_1203_5441.jpg"),
    ]

    randompast = random.choice(result)

    context = {
        "name": name,
        "past": randompast[0],
        "pastimg": randompast[1],
    }

    return render(request, "past-result.html", context)
