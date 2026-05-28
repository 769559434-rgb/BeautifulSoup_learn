# # urlencode应用场景：多个参数的时候
#
# https://www.baidu.com/s?wd=周杰伦&sex=男
#h获取网页源码
import urllib.parse
import urllib.request
import ssl
ssl_context =ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

date = {"wd": "周杰伦",
        "sex": "男",
        "location":"中国台湾省"}

a = urllib.parse.urlencode(date)

#请求资源路径
url = "https://www.baidu.com/s?" + a


#请求对象定制
headers = { "user-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
,"Referer": "https://www.baidu.com/",  # 告诉百度是从首页跳转过来的
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",  # 中文偏好
    "Connection": "keep-alive" } # 保持连接
request = urllib.request.Request(url=url,headers=headers)

#发送请求
response = urllib.request.urlopen(request,context=ssl_context,timeout=10)

#获取响应数据
content = response.read().decode("utf-8")

#输出
print(content)



