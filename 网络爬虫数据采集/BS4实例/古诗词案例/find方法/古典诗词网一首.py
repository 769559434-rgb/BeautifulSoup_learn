import os
import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.gushici.net/t/1/86/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
}
# 读取本地HTML文件（已提前下载）
res = requests.get(url, headers=headers).text

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(res, 'lxml')

# 提取诗词名称（从 <b> 标签中获取）
poem_name = soup.find('b').get_text().strip()

# 提取朝代和作者信息（从 <p class="source"> 中获取）
source_p = soup.find('p', class_='source')

# 第一个 <a> 标签是朝代
dynasty = source_p.find('a').get_text().strip()

# 第二个 <a> 标签是作者姓名
author = source_p.find_all('a')[1].get_text().strip()

# 提取诗词正文内容（从 <div class="gushici-box-text"> 中获取）
poem_content_list = soup.find('div', class_='gushici-box-text')
poem_lines = []
for line in poem_content_list:
    # 去除每行前后空白字符
    poem_lines.append(line.get_text().strip())

# 将诗词内容合并为一个字符串（用换行符分隔）
poem_content = '\n'.join(poem_lines)

# 整理诗词信息到字典中
poem_info = {
    'poem_name': poem_name,
    'dynasty': dynasty,
    'author': author,
    'content': poem_content
}

# 打印诗词信息
print("=" * 50)
print(f"诗词名称: {poem_info['poem_name']}")
print(f"朝代: {poem_info['dynasty']}")
print(f"作者: {poem_info['author']}")
print("-" * 50)
print("诗词内容:")
print(poem_info['content'])
print("=" * 50)
