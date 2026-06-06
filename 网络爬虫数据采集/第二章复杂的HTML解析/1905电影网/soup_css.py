import requests
from bs4 import BeautifulSoup

url='https://www.1905.com/pinglun/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
}
#发送请求
res = requests.get(url=url,headers=headers)
res.encoding = 'utf-8'  # 设置编码
# print(res.text)


#得到响应数据并解析
soup = BeautifulSoup(res.text,'lxml')

title = soup.select('.clearfix li')
# print(title)
abstract = soup.select('.list-txt p')
for i in range(len(title)):
    print(title[i].get_text(strip=True) )  # strip=True 去除首尾空白
    print(abstract[i].get_text(strip=True) )
    print("-" * 50)  # 添加分隔线



