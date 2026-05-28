import  requests

url = "http://www.baidu.com"

response = requests.get(url)
response.encoding="utf-8"

print(response.text)
# print(response.encoding)