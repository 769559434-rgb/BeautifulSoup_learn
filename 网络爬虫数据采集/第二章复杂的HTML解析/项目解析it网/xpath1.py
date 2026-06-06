from lxml import etree

with open("3g.html", "r", encoding="utf-8") as f:
    html = f.read()
    tree = etree.HTML(html)
    title_links = tree.xpath('//*[@id = "content"]/article//div[@itemprop = "image"]/a')
    # 提取 h2 标题中的链接
    href_ = tree.xpath('//*[@id="content"]//article//div/h2/a')
    print(href_)
    print(len(href_))
    # print(title_links)
    for x in href_:
        url =x.get("href")
        print('http:'+url)
        print(x.get("title"))
        print("-" * 50)
        # print(x.xpath("@href")[0])  # 取列表第一个元素
        # print(x.xpath("@title")[0])  # 取列表第一个元素