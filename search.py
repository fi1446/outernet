#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from urllib import request as req
from urllib import error
from urllib import parse
import bs4
import sys

keyword = sys.argv[1]
count = sys.argv[2]

urlKeyword = parse.quote(keyword)
url = 'https://www.google.com/search?hl=jp&q=' + urlKeyword + '&btnG=Google+Search&tbs=0&safe=off&tbm=isch'

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",}
request = req.Request(url=url, headers=headers)
page = req.urlopen(request)

html = page.read().decode('utf-8')
html = bs4.BeautifulSoup(html, "html.parser")
elems = html.select('.rg_meta.notranslate')
counter = 0
for ele in elems:
    ele = ele.contents[0].replace('"','').split(',')
    eledict = dict()
    for e in ele:
        num = e.find(':')
        eledict[e[0:num]] = e[num+1:]
    imageURL = eledict['ou']

    # 今回は、取得した画像をPNG形式にしてしまう
    pal = '.png'

    try:
        img = req.urlopen(imageURL)
        localfile = open("/path/to/image" + count + pal, 'wb')
        localfile.write(img.read())
        img.close()
        localfile.close()
        counter += 1
        if counter == 1:
            break
    except UnicodeEncodeError:
        continue
    except error.HTTPError:
        continue
    except error.URLError:
        continue
