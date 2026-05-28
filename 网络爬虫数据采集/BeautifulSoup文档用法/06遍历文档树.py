from bs4 import BeautifulSoup

with open('ailisi.html', 'r', encoding='utf-8') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'lxml')

# 找到 <head> 标签
# print(soup.head)

# 找到 <title> 标签
# print(soup.title)

# 找到第一个 <a> 标签
# print(soup.a)

# 找到所有 <a> 标签，返回列表
# print(soup.find_all('a'))

# 获取 <head> 标签
# head_tag = soup.head
# print(head_tag)

# 获取 <head> 标签的所有子节点（列表形式）
# print(head_tag.contents)

# 获取 <head> 的第一个子节点（即 <title> 标签）
# title_tag = head_tag.contents[0]
# print(title_tag)

# 获取 <title> 标签的子节点（文本内容）
# print(title_tag.contents)

# 遍历并打印所有去除空白的文本字符串
# for string in soup.stripped_strings:
#     print(repr(string))

# 同时查找所有 <a> 和 <b> 标签
print(soup.find_all(['a', 'b']))
