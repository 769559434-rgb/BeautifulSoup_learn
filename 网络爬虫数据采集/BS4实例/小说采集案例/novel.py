import requests
from bs4 import BeautifulSoup
import time
url = 'https://www.cuxs.org/34352/'

headers = {
    'referer':'https://www.cuxs.org/top/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language':'en,zh-CN;q=0.9,zh;q=0.8',
    'cookie':'_clck=1uqtkl2%5E2%5Eg6h%5E0%5E2341; _clsk=5f64zh%5E1780185213441%5E4%5E1%5Ea.clarity.ms%2Fcollect'

}

res = requests.get(url=url,headers=headers).text
def get_url():
    """获取章节URL列表"""
    soup = BeautifulSoup(res,'lxml')
    #CSS选择器方法
    links = soup.select('ul.section-list li a')
    # print(links)
    urls_list = []
    for link in links[12:17]:
        title = link.get('title')
        href = link.get('href')
        # print(f'章节:{title},URL{href}')
        full_url =  url+href
        urls_list.append(full_url)
        # print(urls)
    return urls_list


def get_content():
    urls = get_url()
    """获取每章内容并保存到TXT"""
    with open ('../find方法/小说内容前5章.txt', 'w', encoding='utf-8')as f:
        for chapter_url in urls:
            time.sleep(1)
            res = requests.get(url=chapter_url,headers=headers).text
            soup = BeautifulSoup(res, 'lxml')
            name = soup.find('h1').get_text()
            content = soup.find_all('p')
            # print(content)
            print(name)
            all_text = '\n'.join(([p.get_text() for p in content]))
            # print(all_text[:-65])
            #写入文件
            f.write(f'{name}\n')
            f.write(all_text[:-50]+'\n')
            f.write('=' * 50 + '\n\n')
            print(f'已保存 {name} 到 小说内容.txt')
        print(f'\n爬取完成！共保存 {len(urls)} 章到 小说内容.txt')

if __name__ == '__main__':
    get_content()