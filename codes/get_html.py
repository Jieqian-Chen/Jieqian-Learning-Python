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
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Error: get_html")

html = get_html("http://www.baidu.com")
print(html)
# with open("C://CJQ/html1.txt", 'w') as f:
#     print(html, file=f)
#     f.close()


