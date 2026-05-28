# https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=40&limit=20

# https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=60&limit=20

# page    1  2  3  4
# start = 0 20 40 60
# start = (page-1)*20

import urllib.request
import urllib.parse
#请求完整url
def create_request(page):
    base_url = "https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&"
    data = {
        "start": (page-1)*20,
        "limit": 20
    }
    date = urllib.parse.urlencode(data)
    url = base_url + date

    #请求对象定制
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
        "Referer": "https://movie.douban.com/",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest" } # 标识 AJAX 请求
#模拟浏览器发送请求
    request = urllib.request.Request(url=url,headers=headers)
    return request

# #获取响应数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content
#保存数据
def save_content(content):
    with open("doubanmove.json","a",encoding="utf-8") as f:
        f.write(content+"\n")


if __name__ == '__main__':
    start_apge = int(input("请输入起始页码："))
    end_page =   int(input("请输入结束页码："))
    for page in range(start_apge,end_page+1):
#创建请求   #每一页都有自己的请求对象定制
        request = create_request(page)
#获取响应数据
        content = get_content(request)
#保存数据
        save_content(content)
print("保存完成")

