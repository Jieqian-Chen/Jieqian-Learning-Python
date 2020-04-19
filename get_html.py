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

def get_html(url, head):
    try:
        r = requests.get(url, headers = head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Error: get_html")

html = get_html("http://www.baidu.com", {"User-Agent":"Mozilla/5.0"})
print(len(html))