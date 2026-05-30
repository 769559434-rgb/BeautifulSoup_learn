import requests
from bs4 import BeautifulSoup
#
url = 'https://www.gushici.net/t/1/86/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
}

# 读取本地HTML文件（已提前下载）
res = requests.get(url, headers=headers).text
# with open('../gushici.html', 'r', encoding='utf-8')as f:
#     res = f.read()
# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(res, 'lxml')
#找到所有诗词块（每个每个<div class="gushici">包含一首诗）
poem_blocks = soup.find_all('div', class_='gushici')
print(f"共有{len(poem_blocks)}首诗词\n")
for i ,block in enumerate(poem_blocks,1):

    # 提取诗词名称（从 <b> 标签中获取）
    poem_name = block.find('b').get_text().strip()
    # 提取朝代和作者信息（从 <p class="source"> 中获取）
    source_p = soup.find('p', class_='source')
    # 第一个 <a> 标签是朝代
    dynasty = source_p.find('a').get_text().strip()
    #第一个 <a> 标签是作者姓名
    author = source_p.find_all('a')[1].get_text().strip()
    # 提取诗词正文内容（从 <div class="gushici-box-text"> 中获取）
    poem_content_list = block.find('div', class_='gushici-box-text')
    poem_lines = []
    for line in poem_content_list:
        # 去除每行前后空白字符
        text = line.get_text().strip()
        #只添加非空文本
        if text:
            poem_lines.append(text)




    # 打印诗词信息
    print("=" * 50)
    print(f"第{i}首")
    print(f"诗词名称: {poem_name}")
    print(f"朝代: {dynasty}")
    print(f"作者: {author}")
    print(f"内容：{poem_lines}")
    print("=" * 50)
