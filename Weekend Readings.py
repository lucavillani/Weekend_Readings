from dis import COMPILER_FLAG_NAMES
from urllib.request import urlopen
from urllib.parse import quote

import webbrowser

url = urlopen('https://collectingwisdom.com/')

keywords = ["monevator", "accidentalfire", "financialsamurai"]

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

x = 0
y = 0
article_list = list()

html = url.read()
html_decoded = html.decode("utf-8")
final_text = html_decoded.split()


for line in final_text:
    if keywords[(0 + x)] in line:
        clean_line = line.replace("href=", "")
        print("\n", clean_line, "\n")
        article_list.append(clean_line)
        x = x + 1
    if x >= len(keywords):
        break


read = input("Do you want to read those articles? [y/n] ")
if read == "y":
    for article in article_list:
        article = article_list[0 + y]
        article_unquoted = article.replace('"', '')
        y = y + 1
        print(article_unquoted)
        webbrowser.get('chrome').open((article_unquoted))


