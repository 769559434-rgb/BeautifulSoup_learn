
import urllib.request
import urllib.parse
url = "https://fanyi.baidu.com/sug"

#请求对象定制为了解决反爬的第一种手段
headers = {
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
"Referer": "https://www.baidu.com/",  # 告诉百度是从首页跳转过来的
    "Accept-Language": "zh-CN,zh;q=0.9",  # 中文偏好
    "Connection": "keep-alive"  # 保持连接
}

data = {"kw":"spide"}

#post的请求参数必须进行编码
data = urllib.parse.urlencode(data).encode("utf-8")
# print(data)

#post的请求的参数，是不会添加到url中的，而是需要放在请求对象定制的参数中
#post请求的参数必须进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)
# print(request)
#模拟浏览器发送请求
response = urllib.request.urlopen(request)
#获取响应的数据
content = response.read().decode("utf-8")
print(content)

#post请求方式的参数必须进行编码 data = urllib.parse.urlencode(data)
#编码之后 必须调用encode方法  data = urllib.parse.urlencode(data).encode("utf-8")
#参数放在请求对象定制参数中  request = urllib.request.Request(url=url,data=data,headers=headers)
