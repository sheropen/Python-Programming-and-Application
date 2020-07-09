import requests
from bs4 import BeautifulSoup

url="http://tech.163.com/"
r = requests.get(url,timeout=30)
r.encoding=r.apparent_encoding
soup = BeautifulSoup(r.text,'lxml')

#Newest-list
print("栏目:最新快讯")
lst = soup.find('div', class_ = "newest-lists")
for news in lst.find_all('li', class_ = 'list_item'):
    info=news.find('a')
    if info:
        title = info.get_text().strip()[:-5].strip()
        link = str(info.get('href'))
        print(f"标题:{title}")
        print(f"链接:{link}\n")
#Hot-list
print("\n栏目：今日热点")
lst = soup.find('div',class_ = 'hot-list')
for news in lst.find_all('a')[:-1]:
    title = news.get_text()
    link = str(news.get('href'))
    print(f"标题:{title}")
    print(f"链接:{link}\n")

#Smart 
print("\n栏目:智能")
lst = soup.find('div',class_='bc_detail')
for news in lst.find_all('a'):
    title = news.get_text().strip()
    link = str(news.get('href'))
    print(f"标题:{title}")
    print(f"链接:{link}\n")

#Smart_detail
print("\n栏目:后厂村7号")
lst = soup.find('div',class_ = 'smart_detail')
for news in lst.find_all('a'):
    title = news.get_text().strip()
    link = str(news.get('href'))
    print(f"标题:{title}")
    print(f"链接:{link}\n")

#Original_plan
print("\n栏目:态℃/科学大师")
lst = soup.find('div',class_ = 'original_plan')
for news in lst.find_all(class_ = 'ac_title'):
    info=news.find('a')
    if info:
        title = info.get_text().strip()
        link = str(info.get('href'))
        print(f"标题:{title}")
        print(f"链接:{link}\n")


