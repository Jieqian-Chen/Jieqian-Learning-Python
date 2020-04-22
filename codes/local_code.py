#!/usr/bin/env python3
import requests
import re
import os

def GetHtmlText(url):
    try:
        kv = {'User-agent':'Mozilla/5.0'}
        r = requests.get(url, headers = kv)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print("Error: GetHtmlText")

def GetMovieMsg(mv_msg,urltext):
    mv_msg = {}
    mv_rank = r'>([\d].*?)</em'
    mv_titlel = r'<span class="title">([^&nbsp;/&nbsp;].*?)</span>'
    mv_score = r'"v:average">(.*?)</span>'
    mv_words = r'"inq">(.*?)</span>'
    mv_star = r'(\b.*?)<br>'
    mv_img_url = r'<img width="100" alt=".*?" src="(.*?)" class="">'

    ls_mv_rank = re.findall(mv_rank,urltext)
    ls_mv_titlel = re.findall(mv_titlel,urltext)
    ls_mv_score = re.findall(mv_score,urltext)
    ls_mv_words = re.findall(mv_words,urltext)
    ls_mv_star = re.findall(mv_star,urltext)
    ls_mv_img_url = re.findall(mv_img_url,urltext)

    mv_msg = {ls_mv_rank, ls_mv_titlel, ls_mv_score, ls_mv_words, ls_mv_star, ls_mv_img_url}
##    print(ls_mv_rank)
##    print(ls_mv_titlel)
##    print(ls_mv_score)
##    print(ls_mv_words)
##    print(ls_mv_star)
##    print(ls_mv_img_url)

    return mv_msg




def main():
    url = "https://movie.douban.com/top250"
    mv = {}
    ls = GetMovieMsg(mv,GetHtmlText(url))
    print(len(ls))

main()
######################################################################################################

#py20200414.py
#!/usr/bin/env python3
#coding=utf-8
##import os
import datetime
filepath = "E://py20200414.txt"
## 获取格式化后的当前日期时间，lib: import datetime
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

intext = input("请输出新增内容：")

## 在文件结尾新增文本内容
with open(filepath,"a") as f:
    print('\n' + date,file = f)
##    print('This is added line',file = f)
    print(intext,file = f)
    f.close()

## 输出文件内容
fo = open(filepath, "r+")
txt = fo.read()
print(txt)
fo.close()

######################################################################################################


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import keyword
keyword.kwlist # 列出所有关键字
keyword.iskeyword('if') # 查询某个词是不是关键字

import requests
url = "https://movie.douban.com/top250"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.encoding)
    print(r.text[:2000])
except:
    print("爬取失败")
######################################################################################################

import os
import requests
from lxml import etree

# 负责下载电影海报
def download_img(db_id, title, img_addr, headers):

    # 如果不存在图片文件夹,则自动创建
    if os.path.exists("./Top250_movie_images/"):
        pass
    else:
        os.makedirs("./Top250_movie_images/")

    # 获取图片二进制数据
    image_data = requests.get(img_addr, headers=headers).content
    # 设置海报存存储的路径和名称
    image_path = "./Top250_movie_images/" + db_id[0] + "_" + title[0] + '.jpg'
    # 存储海报图片
    with open(image_path, "wb+") as f:
        f.write(image_data)



# 根据url获取数据,并打印到屏幕上,并保存为文件
def get_movies_data(url, headers):

    # 获取页面的响应内容
    db_response = requests.get(url, headers=headers)

    # 将获得的源码转换为etree
    db_reponse_etree = etree.HTML(db_response.content)

    # 提取所有电影数据
    db_movie_items = db_reponse_etree.xpath('//*[@id="content"]/div/div[1]/ol/li/div[@class="item"]')

    # 遍历电影数据列表,
    for db_movie_item in db_movie_items:

        # 这里用到了xpath的知识
        db_id = db_movie_item.xpath('div[@class="pic"]/em/text()')
        db_title = db_movie_item.xpath('div[@class="info"]/div[@class="hd"]/a/span[1]/text()')
        db_score = db_movie_item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')
        db_desc = db_movie_item.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()')
        db_img_addr = db_movie_item.xpath('div[@class="pic"]/a/img/@src')
        print("编号:",db_id,"标题:",db_title, "评分:",db_score,"电影描述:", db_desc)
        # a表示追加模式, b表示以二进制方式写入, + 表示如果文件不存在则自动创建
        with open("./douban_movie_top250.txt", "ab+") as f:
            tmp_data = "编号:"+str(db_id)+"标题:"+str(db_title)+"评分:"+str(db_score)+"电影描述:"+ str(db_desc)+"\n"
            f.write(tmp_data.encode("utf-8"))

        db_img_addr = str(db_img_addr[0].replace("\'", ""))
        download_img(db_id, db_title, db_img_addr, headers)


def main():
    # 使用列表生成式,生成待爬取的页面url的列表
    urls = ["https://movie.douban.com/top250?start="+str(i*25) for i in range(10)]

    # 设置请求头
    headers = {
        # 设置用户代理头(为狼披上羊皮)
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    # 为避免重复运行程序,造成内容重复,这里把上次的文件清除(可跳过)
    if os.path.isfile("./douban_movie_top250.txt"):
        os.remove("./douban_movie_top250.txt")

    # 从列表取出url进行爬取
    for url in urls:
        get_movies_data(url, headers)

if __name__ == '__main__':
    main()

######################################################################################################
#!/usr/bin/env python3
import requests
import os
import re

page = 0
url = 'https://movie.douban.com/top250?start=' + str(25 * page) + '&filter='

try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.encoding)
    print(len(r.text))
except:
    print("爬取失败")

html = r.text

mv_rank = r'>([\d].*?)</em'
mv_titlel = r'<span class="title">([^&nbsp;/&nbsp;].*?)</span>'
mv_score = r'"v:average">(.*?)</span>'
mv_words = r'"inq">(.*?)</span>'
mv_star = r'(\b.*?)<br>'
mv_img_url = r'<img width="100" alt=".*?" src="(.*?)" class="">'

ls_mv_rank = re.findall(mv_rank,html)
ls_mv_titlel = re.findall(mv_titlel,html)
ls_mv_score = re.findall(mv_score,html)
ls_mv_words = re.findall(mv_words,html)
ls_mv_star = re.findall(mv_star,html)
ls_mv_img_url = re.findall(mv_img_url,html)

print(ls_mv_rank)
print(ls_mv_titlel)
print(ls_mv_score)
print(ls_mv_words)
print(ls_mv_star)
print(ls_mv_img_url)

mv_img_name = ls_mv_rank[i] + '_' + ls_mv_titlel[i]
print(mv_img_name)

for i in range(len(ls_mv_titlel)):
	print(mv_img_name)

######################################################################################################
import requests
import os
url = "http://image.ngchina.com.cn/2015/0323/20150323111422966.jpg"
root = "E://A_pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers = kv)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
######################################################################################################
#!/usr/bin/env python3
import requests
import re
import os

def GetHtmlText(url):
    try:
        kv = {'User-agent':'Mozilla/5.0'}
        r = requests.get(url, headers = kv)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print("Error: GetHtmlText")

def GetMovieMsg(mv_msg,urltext):
    mv_msg = {}
    mv_rank = r'>([\d].*?)</em'
    mv_titlel = r'<span class="title">([^&nbsp;/&nbsp;].*?)</span>'
    mv_score = r'"v:average">(.*?)</span>'
    mv_words = r'"inq">(.*?)</span>'
    mv_star = r'(\b.*?)<br>'
    mv_img_url = r'<img width="100" alt=".*?" src="(.*?)" class="">'

    ls_mv_rank = re.findall(mv_rank,urltext)
    ls_mv_titlel = re.findall(mv_titlel,urltext)
    ls_mv_score = re.findall(mv_score,urltext)
    ls_mv_words = re.findall(mv_words,urltext)
    ls_mv_star = re.findall(mv_star,urltext)
    ls_mv_img_url = re.findall(mv_img_url,urltext)

    mv_msg = {ls_mv_rank, ls_mv_titlel, ls_mv_score, ls_mv_words, ls_mv_star, ls_mv_img_url}
##    print(ls_mv_rank)
##    print(ls_mv_titlel)
##    print(ls_mv_score)
##    print(ls_mv_words)
##    print(ls_mv_star)
##    print(ls_mv_img_url)

    return mv_msg




def main():
    url = "https://movie.douban.com/top250"
    mv = {}
    ls = GetMovieMsg(mv,GetHtmlText(url))
    print(len(ls))

main()


######################################################################################################
