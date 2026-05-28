import urllib.request
import urllib.parse
import ssl
import json
from urllib.error import URLError, HTTPError

# 创建 SSL 上下文
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# 豆瓣电影排行榜 API
url = "https://movie.douban.com/j/chart/top_list"

# 查询参数
data = {
    "type": "10",  # 类型（10=悬疑）
    "interval_id": "100:90",  # 区间
    "action": "",  # 动作
    "start": "0",  # 起始位置
    "limit": "20"  # 获取数量
}

# 请求头 - 模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "Referer": "https://movie.douban.com/",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "X-Requested-With": "XMLHttpRequest"  # 标识 AJAX 请求
}

try:
    # 编码参数并拼接到 URL
    query_string = urllib.parse.urlencode(data)
    full_url = url  +"?"+ query_string

    print(f"请求 URL: {full_url}")

    # 创建请求对象
    request = urllib.request.Request(url=full_url, headers=headers)

    # 发送 GET 请求
    response = urllib.request.urlopen(request, context=ssl_context, timeout=10)

    # 读取响应数据
    content = response.read().decode("utf-8")

    # 解析 JSON 数据
    data = json.loads(content)

    print(f"状态码：{response.status}")
    print(f"获取到 {len(data)} 部电影\n")
    print("=" * 80)

    # 遍历电影列表
    for index, movie in enumerate(data, 1):
        print(f"{index}. 《{movie['title']}》")
        print(f"   评分：{movie['rating'][0]} ({movie['rating'][1]}人评分)")
        print(f"   类型：{', '.join(movie['types'])}")
        print(f"   上映日期：{movie['release_date']}")
        print(f"   封面：{movie['cover_url']}")
        print("-" * 80)

    # 保存原始 JSON 数据
    with open("douban_movies.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("\n数据已保存到 douban_movies.json")

    response.close()

except HTTPError as e:
    print(f"HTTP 错误：{e.code} - {e.reason}")
    if e.code == 418:
        print("提示：可能被豆瓣反爬虫机制识别了")
except URLError as e:
    print(f"URL 错误：{e.reason}")
except json.JSONDecodeError as e:
    print(f"JSON 解析错误：{e}")
    print(f"响应内容：{content[:200]}")
except Exception as e:
    print(f"发生错误：{e}")
