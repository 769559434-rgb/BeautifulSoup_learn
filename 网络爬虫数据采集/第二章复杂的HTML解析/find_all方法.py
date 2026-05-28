from urllib.request import urlopen
from bs4 import BeautifulSoup

# 打开网页并读取内容
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

# 查找所有class为green的span标签
nameList = bsObj.find_all("span", {"class": "green"})

# 遍历列表，逐个提取文本（每行一个）
for name in nameList:
    print(name.get_text())

# 用列表推导式提取所有文本，去除空白后打印成一个列表
print([name.get_text().strip() for name in nameList])

# 查找id为text的元素（已注释）
# allText = bsObj.find_all(id="text")
# print(allText[0].get_text())