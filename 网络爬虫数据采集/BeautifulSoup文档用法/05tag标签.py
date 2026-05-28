from bs4 import BeautifulSoup

# 解析HTML字符串
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')

# 找到 <b> 标签
tag = soup.b

# 查看标签的类型
print(type(tag))

# 打印标签名称（输出: b）
print(tag.name)

# 修改标签名称为 blockquote
tag.name = 'blockquote'

# 打印修改后的标签（输出: <blockquote class="boldest">Extremely bold</blockquote>）
print(tag)

# 创建新的标签对象
tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b

# 获取标签的 id 属性值（输出: boldest）
print(tag['id'])

# 获取标签的所有属性（输出: {'id': 'boldest'}）
print(tag.attrs)