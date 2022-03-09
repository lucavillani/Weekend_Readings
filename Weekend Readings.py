from dis import COMPILER_FLAG_NAMES
from urllib.request import urlopen
from urllib.parse import quote

import webbrowser

# TARGET WEBSITE
url = urlopen('https://collectingwisdom.com/')
# FAVOURITE BLOGS TO RETRIEVE
keywords = ["monevator", "accidentalfire", "financialsamurai"]

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

x = 0
y = 0
article_list = list()

html = url.read()
html_decoded = html.decode("utf-8")
final_text = html_decoded.split()

print("\n WELCOME TO WEEKEND READINGS \n \n \n Please find below the latest articles from your favorite personal finance bloggers: \n")
# RETRIEVE AND PRINT THE ARTICLES
for line in final_text:
    if keywords[(0 + x)] in line:
        clean_line = line.replace("href=", "")
        print("\n", clean_line, "\n")
        article_list.append(clean_line)
        x = x + 1
    if x >= len(keywords):
        break

print("")
# DO YOU WANT TO OPEN THE ARTICLES?
read = input("Do you want to read those articles? [y/n] ")
if read == "y":
    for article in article_list:
        article = article_list[0 + y]
        article_unquoted = article.replace('"', '')
        y = y + 1
        webbrowser.get('chrome').open((article_unquoted))
    print("\n \n Thank you! You will be shortly redirected to your browser \n \n")


#NEXT STEPS: RETRVIE ARTICLE TITLES