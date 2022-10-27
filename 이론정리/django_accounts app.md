### 1. accounts app 생성 및 등록 

```bash
# 앱 생성
$ python manage.py startapp accounts 

# 앱 등록 
# pjt/settings.py 
INSTALLED_APPS = [
    'accounts',
    ...,
]
```

<br>

### 2. url 분리

```django
# pjt/urls.py 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
```

```django
# accounts/urls.py 생성

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

]
```

<br>

### 3. User model

- Django User Model
  - Custom User Model 로 대체하기
  - Django 는 기본적인 인증 시스템과 여러가지 필드가 포함된 User Model 을 제공, 대부분의 개발 환경에서 기본 User Model 을 Custom User Model 로 대체
  - Django 는 새 프로젝트를 시작하는 경우 비록 기본 User 모델(`auth.User`)이 충분하더라도 커스텀 User 모델(`accounts.User`) 설정하는 것을 강력하게 권장(highly recommended)
  - 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문에 설정하는 것이 좋음
    - 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate 를 실행하기 전에 이 작업을 마쳐야 함
    - 모델을 바꾼다는 것은 DB가 변경된다는 것과 동일한 말이기 때문에, 만약 Custom User Model 을 언제든지 변경할 수 있도록 미리 만들어두지 않으면 나중에 모델 하나 바꾸기 위해 DB를 복잡하게 변경해야 하는 이슈가 발생할 수 있음

#### 3-1. AUTH_USER_MODEL 정의

```django
# pjt/settings.py 에 코드 추가

# User Model
AUTH_USER_MODEL = 'accounts.User'
```

#### 3-2. 내부에 있던 모델 상속 받아오기

```django
# accounts/models.py

'''
아래 내용은 원래 프로젝트 시작할 때 작성해야 되는거니까, 
혹시 이전에 작성되었던 DB(db.sqlite3) 존재하면 삭제하기
migrations 풀더에 __init__.py 제외하고 번호 붙은 파일들도 삭제
'''

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
```

#### 3-3. DB반영

```bash
$ python manage.py makemigrations
$ python manage.py migrate

# 이제 auth_user 테이블이 아니라 accounts_user 테이블 사용시작
```

#### 3-4 관리자 정보 하나 생성

```bash
$ python manage.py createsuperuser
```

<hr>

## 👩🏻‍💻 회원가입 기능 구현

### 1. CREATE

#### 1-1. URL

```python
# accounts/urls.py 

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

#### 1-2. VIEW

```python
# accounts/views.py 

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

#### 1-3. TEMPLATE

```django
<!-- accounts/templates/accounts/signup.html 생성 -->

{% extends 'base.html' %}
{% load django_bootstrap5 %}
  
{% block content %}
  <h1>회원가입</h1>
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form form %}
      {% bootstrap_button button_type="submit" content="OK" %}
  </form>

{% endblock content %}
```

#### 1-4. POST 처리

```python
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:     
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

 #### 1-5. UserCreationForm()

```python
# accounts/forms.py 생성하고, 아래와 같이 내용 채우기
# get_user_model()은 현재 프로젝트에서 활성화된 사용자 모델을 반환

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email')
        labels = {
      'username': '닉네임',
      'password1': '비밀번호',
      'password2': '비밀번호 확인',
      'email' : '이메일'
    }
```

#### 1-6. CustomUserCreationForm반영

````python
# accounts/views.py

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:     
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
````

#### 1-7 admin.py

```python
# accounts/admin.py 

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

admin.site.register(get_user_model(), UserAdmin)
```

<br>

### 2. READ

#### 2-1. URL

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
]
```

#### 2-2 VIEW

```python
# accounts/views.py 

def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)
```

#### 2-3. TEMPLATE

```django
<!-- accounts/templates/accounts/index.html -->

{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block content %}
  <div class="row mt-5">
    <h1 class="text-center">회원목록</h1>
    <!-- Table -->
    <table class="table table-hover mt-3">
      <thead>
        <tr>
          <th scope="col">번호</th>
          <th scope="col">닉네임</th>
          <th scope="col">이메일</th>
        </tr>
      </thead>
      <tbody>
        {% for user in users %}
          <tr>
            <th scope="row">{{ forloop.counter }}</th>
            <td>
              <a href="">{{ user.username }}</a>
            </td>
            <td>{{ user.email }}</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
  <a class="btn btn-primary" href="{% url 'index' %}">처음으로</a>
</div>
{% endblock content %}
```

#### 2-4. (detail page) URL

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.detail, name='detail'),
]
```

#### 2-5. VIEW

```python
def detail(request, pk):
    # user 정보 받아오기
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)
```

#### 2-6. TEMPLATE

```django
<!-- accounts/templates/accounts/detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>{{ user.username }}님의 프로필</h1>
  <p>이메일:{{ user.email }}</p>

{% endblock content %}
```

