"""
@create by Jieqian Chen
@GitHub repository: https://github.com/Jieqian-Chen/Jieqian-Learning-Python
@E-mail: jieqianchen@foxmail.com
@update:
    1. 2020/04/22,
    2. http://www.zuihaodaxue.cn/Greater_China_Ranking2019_0.html
    3. check robots.txt: http://zuihaodaxue.cn/robots.txt, return 404
    4. step.1 get_html
    5. step.2 get_ranking
    6. step.3 print_ranking
    7. pip install beautifulsoup4

"""
import  requests
from bs4 import BeautifulSoup
import bs4


def get_html(url, head = {"User-Agent":"Mozilla/5.0"}):
    try:
        # 使用 headers 时，可以获取的信息更多
        r = requests.get(url, headers = head)
        # 不使用 headers 时，只能获得少量信息，并且很多网站不支持 robots 访问
        # r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Error: get_html")

def get_ranking(ranking_list, html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        for tr in soup.find('tbody').children:
            if isinstance(tr, bs4.element.Tag):
                tds = tr('td')
                ranking_list.append([tds[0].string, tds[1].string, tds[3].string])
        return ranking_list
    except:
        print("Error: get_ranking")

def print_ranking(ranking_list, num):
    for rank in ranking_list[:num]:
        print("{}\t{:10}\t{}".format(rank[0],rank[1],rank[2]))

def main():
    ranking_list = []
    url = "http://www.zuihaodaxue.cn/Greater_China_Ranking2019_0.html"
    html = get_html(url)
    ranking_list = get_ranking(ranking_list, html)
    print_ranking(ranking_list, 20)

main()

