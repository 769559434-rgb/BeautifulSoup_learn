import re

from bs4 import BeautifulSoup

with open('ailisi.html', 'r', encoding='utf-8') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'lxml')
# 可以通过 class_ 参数搜索有指定CSS类名的 tag:
# sitster_ = soup.find_all('a', class_='sister')
# print(sitster_)

#正则表达式查找
# itl = soup.find_all(class_ = re.compile('itl'))
# print(itl)

# 找到所有 class 名称恰好是6个字母的标签（会找到3个 <a> 标签，
# 它们的 class 都是 "sister"）。
# def has_six_characters(css_class):
#     return css_class is not None and len(css_class) == 6
#
# has_six_characters_ = soup.find_all(class_ = has_six_characters)
# print(has_six_characters_)


# 按照 CSS 类名搜索时，表示匹配到 tag 中任意 CSS 类名:
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
# print(css_soup.find_all('p',class_ = "strikeout"))


# 搜索 class 属性时也可以通过 CSS 值进行完全匹配
print(css_soup.find_all('p',class_ = "body strikeout"))


# 使用 CSS 选择器
print(css_soup.select('p.strikeout')[0])

