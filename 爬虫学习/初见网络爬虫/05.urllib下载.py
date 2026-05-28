"""下载图片"""
import urllib.request
import os
url_img ="https://gips3.baidu.com/it/u=3886271102,3123389489&fm=3028&app=3028&f=JPEG&fmt=auto?w=1280&h=960"
url_resp = urllib.request.urlopen(url=url_img)
img_data = url_resp.read()
with open("mv.jpg", "wb")as f:
    f.write(img_data)