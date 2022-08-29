# CSS 

### 1. CSS 문법

a         {  background-color : yellow ;  font-size:16px  ; }

선택자         속성명                  속성값          속성명   속성값  선언끝



###### CSS 선택자

- Html 요소 선택자

  ```html
  <!-- css를 적용할 대상으로 html 요소의 이름을 직접 사용하여 선택 -->
  <style>
      h2 { color: teal; text-decoration: underline; }
  </style>
  ...
  <h2>이 부분에 스타일을 적용합니다.</h2>
  ```

- 아이디 선택자

  ```html
  <!-- 아이디 선택자는 CSS를 적용할 대상으로 특정 요소를 선택할 때 사용
  이 선택자는 웹 페이지에 포함된 여러 요소 중에서 특정 아이디 이름을 가지는 요소만을 선택 -->
  
  <style>
      #heading { color: teal; text-decoration: line-through; }
  </style>
  ...
  <h2 id="heading">이 부분에 스타일을 적용합니다.</h2>
  ```

- 클래스 선택자

  ```html
  <style>
      .headings { color: lime; text-decoration: overline; }
  </style>
  ...
  <h2 class="headings">이 부분에 스타일을 적용합니다.</h2>
  <p>class 선택자를 이용하여 스타일을 적용할 HTML 요소들을 한 번에 선택할 수 있습니다.</p>
  <h3 class="headings">이 부분에도 같은 스타일을 적용합니다.</h3>
  ```

<br>

### 2. CSS 기본 속성

###### 2-1. 색

```html
<style>
    .blue { color: blue; }
    .green { color: green; }
    .silver { color: silver; }
</style>
```



###### 2-2. 배경

###### 	- background-color 속성

```html
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<title>CSS Backgrounds</title>

  <style>
    body { background-color: lightblue; }
    h1 { background-color: rgb(255,128,0); }
    p { background-color: #FFFFCC; }
  </style>

</head>
<body>
	<h1>CSS를 이용한 배경색 설정입니다.</h1>
	<p>각 HTML 요소에 개별적으로 배경색을 설정할 수 있습니다.</p>
</body>
</html>
```

###### 	- background-image 속성

```html
<style>
    body { background-image: url("/examples/images/img_background_good.png"); }
</style>

<!-- 이미지 수평반복 -->
<style>
    body { background-image: url("/examples/images/img_man.png"); background-repeat: repeat-x; }
</style>

<!-- 이미지 수직반복 -->
<style>
    body { background-image: url("/examples/images/img_man.png"); background-repeat: repeat-y; }
</style>

<!-- 이미지 반복 x -->
<style>
    body { background-image: url("/examples/images/img_man.png"); background-repeat: no-repeat; }
</style>
```



###### 2-3. 텍스트

###### 	- color 속성

```html
<style>
    body { color: red; }
    p { color: maroon; }
</style>
```

###### 	- text-align 속성

```html
<style>
    h2 { text-align: left; }
    h3 { text-align: right; }
    h4 { text-align: center; }
</style>
```

###### 	- text-decoration 속성

```html
<style>
    h2 { text-decoration: overline; }
    h3 { text-decoration: line-through; }
    h4 { text-decoration: underline; }
    a { text-decoration: none; }
</style>
```

<br>

### 



