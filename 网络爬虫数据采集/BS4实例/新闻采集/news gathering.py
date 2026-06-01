import requests
from bs4 import BeautifulSoup

# 新闻页面URL
url = 'https://www.bj.chinanews.com.cn/news/2026/0528/102579.html'

# 请求头设置
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
}

# 发送请求并设置编码
res = requests.get(url=url, headers=headers)
res.encoding = 'gbk'  # 设置编码防止乱码

# 解析HTML
soup = BeautifulSoup(res.text, 'lxml')

# 查找所有p标签
title = soup.find_all('p')

# 遍历输出文本内容
for p in title:
    text = p.get_text().strip()  # 去除首尾空格
    if text:  # 过滤空行
        print(text)
