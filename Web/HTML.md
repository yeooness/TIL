# HTML 

### 1. HTML 기본구조 

- < !DOCTYPE html> : 현재 문서가 HTML5문서임을 명시 
- < html> : HTML 문서의 루트 요소 정의
- < head> : HTML 문서의 메타데이터 정의 
- < title> : HTML 문서의 제목 정의 
- < body> : 웹 브라우저를 통해 보이는 내용 부분 
-  < h1>~< h6> : 제목(heading)
- < p> : 단락(paragraph) 

<br>

### 2. HTML 텍스트 요소

###### 2-1. 제목(Heading)	

```html
<h1>제목1의 크기입니다!</h1>

<h2>제목2의 크기입니다!</h2>

<h3>제목3의 크기입니다!</h3>

<h4>제목4의 크기입니다!</h4>

<h5>제목5의 크기입니다!</h5>

<h6>제목6의 크기입니다!</h6>
```

###### 	<br>

###### 2-2. 단락(Paragraph)

```html
<h1>제목1의 크기입니다!</h1>

<h2>제목2의 크기입니다!</h2>

<h3>제목3의 크기입니다!</h3>

<p>여기서부터 단락입니다.</p>
```

###### 	- 띄어쓰기와 줄 나누기 

```html
<p>

줄을 나누고 싶어서<br>

이렇게 줄을 나눠봤습니다.<br>

<br>

br 태그는 종료 태그가 없는 빈 태그 입니다.

</p>
```

	###### 	-  텍스트 서식 미리 정하기

```html
<pre>
html 코드에서 작성한 텍스트 서식을 그대로 표현하려면 <pre> 태그를 사용해야함
<pre>태그 내에 작성된 텍스트의 모든 띄어쓰기와 줄 나누기는 웹 브라우저에 그대로 표현됨
</pre>
```

###### 	- 수평 가로 구분선

```html
<p>저는 하나의 단락입니다.</p>

<hr>

<p>저는 하나의 단락입니다.</p>

<hr>

<p>저는 하나의 단락입니다.</p>
```

<br>

###### 2-3. 서식

###### 	- 강조 효과 

```html
<p><b>"이 부분"</b>은 단순히 글씨가 굵은 부분이에요!</p>

<p><strong>"이 부분"</strong>은 중요한 부분이라서 굵게 표현됐어요!</p>


<p><i>"이 부분"</i>은 단순히 글씨가 이탤릭체인 부분이에요!</p>

<p><em>"이 부분"</em>은 중요한 부분이라서 이탤릭체로 표현됐어요!</p>
```

###### 	- 하이라이팅 효과

```html
<p><mark>"이 부분"</mark>만 하이라이팅하고 싶어요.</p>
```

###### 	- 삭제 효과

```html
<p><del>"이 부분"</del>을 지운 것처럼 하고 싶어요.</p>
```

###### 	- 삽입 효과

```html
<p><ins>"밑줄 친 부분"</ins>에 들어갈 알맞은 말을 고르세요.</p>
```

###### 	- 위첨자와 아래첨자 효과

```html
<p>X<sup>2</sup> + Y<sup>3</sup> = Z</p>

<p>물을 나타내는 화학식은 H<sub>2</sub>O 입니다.</p>
```

<br>

###### 2-4. 인용구

###### 	- 짧은 인용구

​      <q> 태그 사용, 자동으로 앞 뒤 큰 따옴표가 붙음 

```html
<p>HTML의 정의는

<q>웹 페이지를 만들기 위한 하이퍼텍스트 마크업 언어</q>

입니다.</p>
```

###### 	- 블록 인용구

```html
<p>HTML의 정의</p>

<blockquote>

인터넷 서비스의 하나인 월드 와이드 웹을 통해 볼 수 있는 문서를 만들 때 사용하는 프로그래밍 언어의 한 종류이다.

</blockquote>
```

###### 	- 축약형 표현

​      <abbr> 태그 위에 마우스를 위치시키면 title 속성에 명시한 용어의 원형이 나타남 

```html
<p><strong><abbr title="HyperText Markup Language 5">HTML5</abbr></strong>

란 웹 문서를 제작하는 데 쓰이는 프로그래밍 언어인 HTML의 최신규격입니다.</p>
```

###### 	- 주소 표현

​	 주소는 이탤릭체로 표현, 위아래로 약간의 공백이 자동 삽입 

```html
<address>

    서울특별시<br>

    강남구 테헤란로

</address>
```

<br>

###### 2-5 주석

```html
<!-- 작성자 : 홍길동 -->

<p>이 부분은 조금 어려운 코드입니다.</p>

<!--

    위와 같이 어려운 코드의 이해를 돕기 위해서 개발자가 적어놓은 설명입니다.

-->
```

<br>

### 3. HTML 기본요소

###### 3-1. 스타일

```html
<태그이름 style="속성이름:속성값">
  
<h1 style="background-color:white; color:maroon; font-size:150%; text-align:center">

    style 속성을 이용하여 한 번에 스타일링 하기!

</h1>
```

<br>

###### 3-2. 색

```html
<h1 style="color:blue">색상 이름으로 표현된 파란색</h1>

<h1 style="color:green">색상 이름으로 표현된 녹색</h1>

<h1 style="color:silver">색상 이름으로 표현된 은색</h1>

<h1 style="color:teal">색상 이름으로 표현된 청록색</h1>

<h1 style="color:red">색상 이름으로 표현된 빨간색</h1>
```

<br>

###### 3-3. 배경

```html
<!-- 배경을 다른 색으로 변경 -->
<style>
    body { background-color: lightblue; }
    h1 { background-color: rgb(255,128,0); }
    p { background-color: #FFFFCC; }
</style>123

<!-- 배경을 다른 이미지로 변경 -->
<body background="/examples/images/img_background_good.png">

...

</body>
```

<br>

###### 3-4. 링크

```html
<a href="링크주소">HTML 링크</a>
<a href="/html/intro">
    <h2>이 링크를 클릭해 보세요!</h2>
</a>

<!-- 링크의 상태 -- >
<style>
		<!-- 아직 한번도 방문한 적이 없는 상태(기본설정) -->
    a:link    { color: teal; }
		<!-- 한번이라도 방문한 적이 있는 상태 -->
    a:visited { color: maroon; text-decoration: none }
		<!-- 링크위에 마우스를 올려놓은 상태 -->
    a:hover   { color: yellow; text-decoration: none }
		<!-- 링크를 마우스로 누르고 있는 상태 -->
    a:active  { color: red; text-decoration: none }
</style>

<!-- 페이지 책갈피 -->
<a href="#bookmark"><p>제목 3으로 갑시다!!!</p></a>

...

<h2><a name="bookmark"></a>제목 3</h2>
```

<br>

###### 3-5. 이미지

```html
<img src="이미지주소" alt="대체문자열">
<img src="/img_html5_logo.png" alt="이미지가 없나봐요..">
```

###### 	- 이미지 크기 설정

```html
<style>
    img {
        width:100%;
        border: 1px solid black;
    }
</style>

...

<img src="/examples/images/img_flag.png" alt="html size" width="320" height="214">
<img src="/examples/images/img_flag.png" alt="style size" style="width:320px; height:214px">
```

###### 	- 이미지 테두리 설정

```html
<img src="/examples/images/img_flag.png" alt="이미지 테두리"
    style="width:320px; height:214px; border: 3px solid black">
```

###### 	- 이미지 링크 설정

```html
<a href="/html/intro" target="_blank">
    <img src="/examples/images/img_flag.png" alt="flag" style="width:320px; height:214px">
</a>
```

<br>

###### 3-6. 리스트

###### 	- 순서가 없는 리스트

```html
<ul>
    <li>사과</li>
    <li>멜론</li>
    <li>바나나</li>
</ul>

<!-- 마커모양 변경 가능 -->
<!-- disc : 기본설정 
     circle : 흰색 작은 원 
     square : 사각형 모양 -->
<ul style="list-style-type: circle">
    <li>수박</li>
    <li>참외</li>
    <li>옥수수</li>
</ul>
<ul style="list-style-type: square">
    ...
</ul>
```

###### 	- 순서가 있는 리스트

```html
<ol>
    <li>사과</li>
    <li>멜론</li>
    <li>바나나</li>
</ol>

<!-- 마커모양 변경 가능 -->
<!-- decimal : 숫자 (기본설정)
     upper-alpha : 영문 대문자
     lower-alpha : 영문 소문자
     upper-roman : 로마 숫자 대문자
     lower-roman : 로마 숫자 소문자 -->
<ol style="list-style-type: upper-alpha">
    <li>수박</li>
    <li>참외</li>
    <li>옥수수</li>
</ol>
<ol style="list-style-type: lower-alpha">
    ...
</ol>
<ol style="list-style-type: upper-roman">
    ...
</ol>
<ol style="list-style-type: lower-roman">
    ...
</ol>
```

###### 	- 정의 리스트

​		<dt> 용어의 이름, <dd> 해당 용어에 대한 정의 

```html
<dl>
    <dt>호박</dt>
    <dd>- 박과의 한해살이 덩굴성 채소</dd>
    <dt>상추</dt>
    <dd>- 국화과의 한해살이 또는 두해살이풀</dd>
</dl>
```

<br>

###### 3-7. 테이블

<tr>태그는 테이블에서 열을 구분해 줍니다.

<th>태그는각 열의 제목을 나타내며, 모든 내용은 자동으로 굵은 글씨에 가운데 정렬이 됩니다.

<td>태그는 테이블의 열을 각각의 셀(cell)로 나누어 줍니다.

```html
<table style="width:100%">
    <tr style="background-color:lightgrey">
        <th>참치</th>
        <th>고래</th>      
    </tr>
    <tr>
        <td>상어</td>
        <td>문어</td>
    </tr>
    <tr>
        <td>오징어</td>
        <td>고등어</td>
    </tr>
</table>
```

