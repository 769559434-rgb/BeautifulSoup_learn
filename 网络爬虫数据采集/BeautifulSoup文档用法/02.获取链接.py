from bs4 import BeautifulSoup
with open('ailisi.html','r',encoding='utf-8') as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())

links=soup.find_all('a')
for link in links:
    print(link.get('href'))

print(soup.get_text())