import os
import requests
from lxml import html
import requests
import bs4
import re

url  = "https://spee.ch/@KhanAcademy:5fc52291980268b82413ca4c0ace1b8d749f3ffb/algebra-linear-equations-3-linear"
page = requests.get(url)
tree = str(bs4.BeautifulSoup(page.text,'lxml'))
#string = '"outpoint":"3ea97f5041538201ad7dc2580edfc8a20d6104a5645577868512be163ef4c6b9:0"'
pattern = r'"outpoint":"[\w\d]+:\d*"'
x = re.search(pattern, tree)
findin = str(x.group()).replace('"','')
print(findin)
pat2 = r"https://spee.ch/@\w+:\d"
pat2 = r"(https://spee.ch/@\w+:[\d\w])[\w\d]+(/[\w\-]*)"
x = re.search(pat2, url)
find2 = str(x.group(1))
find3 = str(x.group(2))+'.mp4?'

print(find2+find3+findin)

