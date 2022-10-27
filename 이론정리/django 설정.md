### 1. 가상환경 생성 및 실행 

```bash
$ python -m venv venv(가상환경이름)
$ source venv(가상환경이름)/bin/activate (맥북)
  source venv/scripts/activate (윈도우)
$(venv)
```

<br>

### 2. Django, Bootstrap5 설치

```bash
$ pip install django==3.2.13
$ pip install django-bootstrap5
$ pip freeze > requirements.txt 

-- 전에 기록해둔 패키지들을 그대로 설치하여 사용할 수 있음 
$ pip install -r requirements.txt 
```

<br>

### 3. Django 프로젝트 생성

```bash
$ django-admin startproject pjt(프로젝트 이름) .(현재 경로에)

# 서버 실행 확인 
$ python manage.py runserver
```

<br>

### 4. 추가 설정 

```django
# pjt/settings.py

INSTALLED_APPS = [
    'django_bootstrap5',
    ...,
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```



### 4-1. base.html

(1) templates 폴더 생성

(2) templates 폴더 안에 base.html 파일 생성 

(3) settings.py 에 등록 

```django
TEMPLATES = [{
	'DIRS': [BASE_DIR/"templates"],
}]
```

```django
#base.html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- CSS only -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
  <title>Document</title>
</head>

<body>
  <!-- Navbar -->


  <div class="container">
    {% block content %}{% endblock content %}
  </div>

  <!-- JavaScript Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3"
    crossorigin="anonymous"></script>
</body>

</html>
```

