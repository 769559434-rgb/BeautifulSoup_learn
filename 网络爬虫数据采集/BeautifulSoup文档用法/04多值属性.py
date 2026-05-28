from bs4 import BeautifulSoup

css_soup = BeautifulSoup('<p class="body"></p>', 'lxml')
print(css_soup.p['class'])


css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
print(css_soup.p['class'])




id_soup = BeautifulSoup('<p id="my id"></p>', 'lxml')
print(id_soup.p['id'])

rel_soup =  BeautifulSoup('<p>Back to the <a rel="index first">homepage</a></p>', 'lxml')
print(rel_soup.a['rel'])
rel_soup.a['rel'] = ['index','contents']
print(rel_soup.p)

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print(type(comment))
print(comment)
