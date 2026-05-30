import csv
import os
import requests
from bs4 import BeautifulSoup


def get_poem_blocks():
    """获取网页并解析出诗词块"""
    url = 'https://www.gushici.net/t/1/86/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
    }
    
    # 读取本地HTML文件（已提前下载）
    res = requests.get(url, headers=headers).text
    # with open('../gushici.html', 'r', encoding='utf-8') as f:
    #     res = f.read()
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(res, 'lxml')
    # 使用CSS选择器找到所有诗词块（每个<div class="gushici">包含一首诗）
    poem_blocks = soup.select('div.gushici')
    print(f"共有{len(poem_blocks)}首诗词\n")
    
    return poem_blocks


def parse_poem(block):
    """解析单个诗词块，返回诗词数据"""
    # 提取诗词名称（从 <b> 标签中获取）
    poem_name = block.select_one('b').get_text().strip()
    
    # 提取朝代和作者信息（从 <p class="source"> 中获取）
    source_p = block.select_one('p.source')
    
    # 第一个 <a> 标签是朝代
    dynasty = source_p.select('a')[0].get_text().strip()
    
    # 第二个 <a> 标签是作者姓名
    author = source_p.select('a')[1].get_text().strip()
    
    # 提取诗词正文内容（从 <div class="gushici-box-text"> 中获取）
    poem_content_div = block.select_one('div.gushici-box-text')
    poem_lines = []
    # 获取div内的文本并按行分割
    text = poem_content_div.get_text().strip()
    if text:
        poem_lines.append(text)
    
    content_str = '\n'.join(poem_lines) if poem_lines else ''
    
    return poem_name, dynasty, author, content_str


def save_to_csv(poem_blocks):
    """保存诗词数据到CSV文件"""
    # 准备CSV文件路径
    csv_path = os.path.join(os.path.dirname(__file__), '10首古诗词简单函数版.csv')
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # 写入表头
        writer.writerow(['序号', '诗词名称', '朝代', '作者', '内容'])
        
        for i, block in enumerate(poem_blocks, 1):
            poem_name, dynasty, author, content_str = parse_poem(block)
            # 写入CSV文件
            writer.writerow([i, poem_name, dynasty, author, content_str])
    
    print("数据已保存到CSV文件：", csv_path)


def display_poems(poem_blocks):
    """在控制台显示诗词信息"""
    for i, block in enumerate(poem_blocks, 1):
        poem_name, dynasty, author, content_str = parse_poem(block)
        
        # 打印诗词信息
        print("=" * 50)
        print(f"第{i}首")
        print(f"诗词名称: {poem_name}")
        print(f"朝代: {dynasty}")
        print(f"作者: {author}")
        print(f"内容：{content_str}")
        print("=" * 50)


# 主程序
poem_blocks = get_poem_blocks()
display_poems(poem_blocks)
save_to_csv(poem_blocks)
