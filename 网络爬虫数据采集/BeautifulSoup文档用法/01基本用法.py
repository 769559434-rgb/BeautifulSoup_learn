from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, "lxml")

# 格式化输出HTML（美化显示）
print(soup.prettify())

# 找到 <title> 标签
print(soup.title)

# .name 属性返回的是标签本身的名称（不带尖括号）
print(soup.title.name)

# 获取 <title> 标签内的文本内容
print(soup.title.string)

# 获取 <title> 父标签的名称（即 head）
print(soup.title.parent.name)

# 找到第一个 <p> 标签
print(soup.p)

# 获取 <p> 标签的 class 属性值
print(soup.p['class'])

# 找到第一个 <a> 标签
print(soup.a)

# 找到所有 <a> 标签，返回列表
print(soup.find_all('a'))

# 查找 id 为 link3 的元素
print(soup.find(id='link3'))