# -*- coding: UTF-8 -*-

import urllib2
import urllib
import re

page = 1
url = "https://www.qiushibaike.com/hot/page/" + str(page)
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
headers = {"User-Agent": agent}

# try:
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
content = response.read()

# pattern = re.compile('<div.*?author clearfix">.*?<a.*?<image.*?></a.*<a.*h2>(.*?)/h2></a>')
pattern = re.compile('<div class="author clearfix">.*?<a.*?<img.*?</a>.*?<a.*?>.*?<h2>.*?(.*?)</h2>', re.S)
items = re.findall(pattern, content)
print 222, items
print 333, len(items)
print items[0]
# for i in xrange(len(items)):
#     print '---------------', i
#     print items[i]
# except urllib2.URLError, e:
#     print 111,  e
