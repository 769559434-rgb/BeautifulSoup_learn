from urllib.request import urlopen
from bs4 import BeautifulSoup

# 打开网页并读取内容
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

# 遍历表格的所有子标签（已注释）
# for child in bsObj.find("table",{"id":"giftList"}).children:
#     print(child)

# 从表格的第二行开始遍历（跳过表头）（已注释）
# for child in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(child)

# 找到特定图片，定位到它的父标签，再找前一个兄弟标签，提取文本
print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())