from bs4 import BeautifulSoup

with open('ailisi.html', 'r', encoding='utf-8') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'lxml')
