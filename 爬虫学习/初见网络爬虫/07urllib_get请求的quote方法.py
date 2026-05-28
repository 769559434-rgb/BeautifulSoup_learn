# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&rsv_spt=1&rsv_iqid=0xabff85df0005a626&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=12&rsv_sug1=11&rsv_sug7=101&rsv_btype=i&prefixsug=%25E5%2591%25A8%25E6%259D%25B0%25E4%25BC%25A6&rsp=3&inputT=2947&rsv_sug4=3704&rsv_sug=1

#需求 获取https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&rsv_spt=1
import urllib.request
import urllib.parse
import ssl
# 创建 SSL 上下文
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False  # 不检查主机名
ssl_context.verify_mode = ssl.CERT_NONE  # 不验证证书



# url ="https://www.baidu.com/s?wd=周杰伦"

#请求对象定制为了解决反爬的第一种手段
headers = {
    "user-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
,"Referer": "https://www.baidu.com/",  # 告诉百度是从首页跳转过来的
    "Accept-Language": "zh-CN,zh;q=0.9",  # 中文偏好
    "Connection": "keep-alive"  # 保持连接
}


name = urllib.parse.quote(input("请输入歌手名称:"))

url = "https://www.baidu.com/s?wd=" + name
#请求对象的定制
request = urllib .request.Request(url=url,headers=headers)

#模拟浏览器发送请求
response = urllib.request.urlopen(request, timeout=10,context =ssl_context)
content = response.read().decode("utf-8")
#输出数据
print(content)
