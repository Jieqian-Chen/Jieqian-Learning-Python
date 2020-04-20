"""
@create by Jieqian Chen
@GitHub repository: https://github.com/Jieqian-Chen/Jieqian-Learning-Python
@E-mail: jieqianchen@foxmail.com
@update:
"""
import requests
import os
def save_url_image(url):
    try:
        img = requests.get(url, headers = {'user-agent':'Mozilla/5.0'})
        with open(path, 'wb') as i:
            i.write(img.content)
            i.close()
            print("save_url_image ok.")
    except:
        print("Error: save_url_image.")

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
    print("Error: save_url_image.")