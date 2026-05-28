import urllib
import urllib.request
from lxml import etree
import urllib.parse
from urllib import error
import lxml.html
import os
import time


#xpath 解析数据
#（1） 本地文件
#（2） 服务器响应的数据 response.read().decode("utf-8")

#小说站点的URL
novel_base_url = "https://www.blqukan.cc/"

#获取小说的URL 拼接完整的URL
novel_url = urllib.parse.urljoin(novel_base_url,"/0_790/")

#每章小说的URL
chapter_url_list=  []

#请求头
headers = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
,"Accept-Language": "zh-CN,zh;q=0.9",  # 中文偏好
    "Connection": "keep-alive"  # 保持连接
}

#获取章节链接列表
def fetch_chapter_urls():
    req = urllib.request.Request(url=novel_url,headers=headers)
    html = lxml.html.parse(urllib.request.urlopen(req))

    hrefs = html.xpath("//dd/a/@href")

    #/html/body/div[5]/dl/dd[13]/a
    #/html/body/div[5]/dl/dd[14]/a
    #/html/body/div[5]/dl/dd[15]/a

    for href in hrefs[12:]:
        chapter_url_list.append(urllib.parse.urljoin(novel_base_url, href))
    print(chapter_url_list)
novel_save_dir = os.path.join(os.getcwd(),"novel_cache/")

#解析每个页面获得的章节正文
def parsing_chapter(url):
    req = urllib.request.Request(url=url,headers=headers)
    html = lxml.html.parse(urllib.request.urlopen(req))
    title = html.xpath("//div/h1/text()")[0]
    contents = html.xpath("//div[@id='content']/text()")
    content = ""
    for i in contents:
        content += i.strip()
    save_novel(title,content)

#把章节正文写到本地
def save_novel(name,content):
    try:
        with open(novel_save_dir+name+".txt","w",encoding="utf-8") as f:
            f.write(content)
    except(urllib.error.HTTPError) as reason:
        print(str(reason))
    else:
        print("下载完成："+name)
if __name__ == '__main__':
    #判断存储的文件夹是否存在，不存在则创建
    if not os.path.exists(novel_save_dir):
        os.mkdir(novel_save_dir)
    #爬取小说文章链接列表
    fetch_chapter_urls()
    #遍历抓取所有的小说内容
    for chapter in chapter_url_list:
        #定时休眠5秒防止IP被封
        time.sleep(5)
        parsing_chapter(chapter)