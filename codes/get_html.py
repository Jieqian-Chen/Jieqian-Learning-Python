"""
@create by Jieqian Chen
@GitHub repository: https://github.com/Jieqian-Chen/Jieqian-Learning-Python
@E-mail: jieqianchen@foxmail.com
@update:
    please add hear:
    2.
    1. 2020/04/20 9:57 create file
"""

import requests

def get_html(url, head = {"User-Agent":"Mozilla/5.0"}):
    try:
        # 使用 headers 时，可以获取的信息更多
        r = requests.get(url, headers = head)
        # 不使用 headers 时，只能获得少量信息，并且很多网站不支持 robots 访问
        # r = requests.get(url)
        # print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Error: get_html")

html = get_html("http://www.baidu.com")
# print(html)
with open("C://CJQ/html1.html", 'w', encoding = "utf-8") as f:
    print(html, file=f)
f.close()

#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

"""
解决UnicodeEncodeError: gbk codec cant encode character \\xa0 in position 0问题_python_python的神奇之旅-CSDN博客
https://blog.csdn.net/weixin_42670402/article/details/82382436
在Python中将网址写入文件的时候，

会碰到：UnicodeEncodeError: ‘gbk’ codec can’t encode character ‘\xa0’ in position 0这个问题。

其实就是在windows中，新建的文本文件的默认编码是gbk.

如此,我们可以在程序中提前指定编码就可以了. 而utf-8通用,就选它了 …….

f = open(‘a.txt’, ‘w’,encoding=’utf-8’)
"""



