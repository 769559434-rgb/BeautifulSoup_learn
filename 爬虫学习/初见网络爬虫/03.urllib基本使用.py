# from urllib.request import urlopen
# from bs4 import  BeautifulSoup
# # html = urlopen('https://www.baidu.com')
# # bsObj = BeautifulSoup(html.read(),"html.parser")
# # print(bsObj.title)
#
# try:
#     html = urlopen("https://www.baidu.com")
# except HTTPError as e:
#     print(e)
#     #返回值为None，终端程序，或者执行另外一个方案
# else:

# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
# from bs4 import BeautifulSoup
# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except (HTTPError, URLError) as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read(),"html.parser")
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
# title = getTitle("http://www.pythonscraping.com/pages/page1.html")
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(),"html.parser")
nameList = bsObj.find_all("span",{"class":"green"})
for name in nameList:
    print(name.get_text())

