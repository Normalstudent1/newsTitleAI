import requests
from bs4 import BeautifulSoup

l=["politics","economy","market-plus","industry","culture","entertainment","sports"]

for k in l:
    f=open("{}.txt".format(k), "w",encoding='utf-8')
    for j in range(1, 21):
        url = 'https://www.yna.co.kr/{0}/all/{1}'.format(k,j)
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            for i in range(1,6):
                f.write(soup.select_one('#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child({}) > div > div.news-con > a > strong'.format(i)).get_text())
                f.write("\n")
            for i in range(7,27):
                f.write(soup.select_one('#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child({}) > div > div.news-con > a > strong'.format(i)).get_text())
                f.write("\n")
        else : 
            print(response.status_code)
    f.close()