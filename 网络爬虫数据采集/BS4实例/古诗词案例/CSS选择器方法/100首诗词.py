import requests
from bs4 import BeautifulSoup
import os
import time

def fetch_page(page):
    """请求单个页面，返回HTML内容"""
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
    }

    # 第1页的URL是index.html，其他页是index_2.html、index_3.html等
    if page == 1:
        url = 'https://www.gushici.net/t/1/86/index.html'
    else:
        url = f'https://www.gushici.net/t/1/86/index_{page}.html'

    print(f'正在爬取第{page}页: {url}')

    # 发送GET请求获取网页内容
    res = requests.get(url, headers=headers)
    return res.text


def parse_poem(block):
    """解析单个诗词块，返回诗词数据"""
    # 提取诗词名称（从<b>标签中获取）
    poem_name = block.select_one('b').get_text().strip()

    # 提取朝代和作者信息（从<p class="source">中获取）
    source_p = block.select_one('p.source')
    dynasty = source_p.select('a')[0].get_text().strip()  # 第一个<a>是朝代
    author = source_p.select('a')[1].get_text().strip()   # 第二个<a>是作者

    # 提取诗词正文内容（从<div class="gushici-box-text">中获取）
    poem_content_div = block.select_one('div.gushici-box-text')
    content = poem_content_div.get_text().strip()

    # 返回字典格式的诗词数据
    return {
        'name': poem_name,
        'dynasty': dynasty,
        'author': author,
        'content': content
    }


def parse_page(html):
    """解析整个页面，返回所有诗词列表"""
    # 使用BeautifulSoup解析HTML，lxml是解析器
    soup = BeautifulSoup(html, 'lxml')

    # 使用CSS选择器找到所有诗词块（每个div.gushici包含一首诗）
    poem_blocks = soup.select('div.gushici')

    all_poems = []
    # 遍历每个诗词块，调用parse_poem解析
    for block in poem_blocks:
        poem_data = parse_poem(block)
        all_poems.append(poem_data)

    return all_poems


def save_to_txt(poems, txt_path):
    """保存诗词到TXT文件"""
    # 以写入模式打开文件，使用utf-8编码支持中文
    with open(txt_path, 'w', encoding='utf-8') as f:
        # 遍历所有诗词，enumerate从1开始计数
        for i, poem in enumerate(poems, 1):
            f.write('=' * 50 + '\n')  # 写入分隔线
            f.write(f'第{i}首\n')     # 写入序号
            f.write(f'诗词名称: {poem["name"]}\n')  # 写入诗词名称
            f.write(f'朝代: {poem["dynasty"]}\n')   # 写入朝代
            f.write(f'作者: {poem["author"]}\n')    # 写入作者
            f.write(f'内容:\n{poem["content"]}\n')  # 写入内容
            f.write('=' * 50 + '\n\n')  # 写入分隔线和空行
    
    print(f'数据已保存到TXT文件: {txt_path}')


def get_all_poems():
    """获取所有页面的诗词"""
    all_poems = []

    # 循环请求10个页面（从第1页到第10页）
    for page in range(1, 11):
        # 请求页面
        html = fetch_page(page)
        
        # 解析页面
        poems = parse_page(html)
        
        # 添加到总列表
        all_poems.extend(poems)

        print(f'第{page}页爬取完成，共{len(poems)}首诗词\n')
        # 休眠4
        if page<10: #最后一页不休眠
            print("等待4秒.....\n")
            time.sleep(4)
    return all_poems


# ===== 主程序执行部分 =====
if __name__ == '__main__':

    # 调用函数，爬取所有诗词
    poems = get_all_poems()
    print(f'总共爬取了{len(poems)}首诗词')

    # 生成TXT文件路径（保存在当前脚本所在目录）
    txt_path = os.path.join(os.path.dirname(__file__), '100首诗词.txt')
    # 调用函数，保存到TXT文件
    save_to_txt(poems, txt_path)
