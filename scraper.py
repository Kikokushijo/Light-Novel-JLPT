import urllib.request
from bs4 import BeautifulSoup
import ssl
import json
import os
import codecs

page_num = 10
os.makedirs('corpus', exist_ok=True)

for page in range(1, page_num+1):
    print('Scraping Page %d...' % page)
    url = "https://yomou.syosetu.com/search.php?&order=hyoka&notnizi=1&p=" + str(page)
    context = ssl._create_unverified_context()
    html = urllib.request.urlopen(url, context=context)
    content = html.read().decode('utf-8')
    #print(content)

    htmlbs = BeautifulSoup(content, "html.parser")
    #print(htmlbs)

    novels = htmlbs.findAll("a", {"class":"tl"})
    novelsurl = []
    #print(novels)
    for novel in novels:
        novelsurl += [[novel.get_text(), novel.attrs["href"]]]
        #print([novel.get_text(), novel.attrs["href"]])
    for novel in novelsurl:
        #print(novel)
        _html = urllib.request.urlopen(novel[1], context=context)
        _content = _html.read().decode('utf-8')
        _htmlbs = BeautifulSoup(_content, "html.parser")

        subs = _htmlbs.findAll("dl", {"class":"novel_sublist2"})
        subsurl = []
        i = 0
        os.makedirs(os.path.join('corpus', novel[0]), exist_ok=True)
        for sub in subs:
            #print(sub)
            subsurl += [[sub.dd.a.get_text(), sub.dd.a.attrs["href"]]]
            #print(sub.dd.a.attrs["href"])

        for sub in subsurl:
            __html = urllib.request.urlopen("https://ncode.syosetu.com" + sub[1], context=context)
            __content = __html.read().decode('utf-8')
            __htmlbs = BeautifulSoup(__content, "html.parser")

            try:

                text = __htmlbs.find("div", {"class":"novel_view"}).get_text()
                #print(sub[0])
                #print(text)
                #input()

                foldername = os.path.join(os.path.join('corpus', novel[0]), str(i) + '.txt')
                # with codecs.open(os.path.join(novel[0], str(i) + ".txt"), 'w+', encoding="utf-8") as f:
                with codecs.open(foldername, 'w+', encoding="utf-8") as f:
                    #json.dumps(text, f)
                    f.write(text)

                print("saved: " + novel[0] + " - " + str(i) + ".txt")

            except:

                print("Error when saved: " + novel[0] + " - " + str(i) + ".txt")
                print("Skipped")

            i += 1
