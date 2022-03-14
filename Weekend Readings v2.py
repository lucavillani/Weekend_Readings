import urllib.request, urllib.parse, urllib.error
import webbrowser

fhand = urllib.request.urlopen("https://collectingwisdom.com")

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

keywords = ["awealthofcommonsense","financialsamurai","monevator", "accidentalfire"]

article_list = list()

def retrieve_and_print():
    count = 0
    global article_list
    for line in fhand:
        line = (line.decode())
        if keywords[count] in line:
            link = line.partition("href=")[2].partition(" target")[0]
            title = line.partition('class="">')[2].partition("</a>")[0]
            print(title, "--->", link, "\n")
            article_list.append(link)
            count += 1
        if count >= len(keywords):
            break 

# DO YOU WANT TO OPEN THE ARTICLES?
def open_in_browser():
    global article_list
    read = input("Do you want to read those articles? [y/n] ")
    if read == "y":
        for article in article_list:
            article_read=article.strip('""')
            webbrowser.get('chrome').open((article_read))
        print("\n \nThank you! You will be shortly redirected to your browser \n \n")
    else:
        quit()

print("\n WELCOME TO WEEKEND READINGS \n \n \n Please find below the latest articles from your favorite personal finance bloggers: \n")
retrieve_and_print()
open_in_browser()
quit()

