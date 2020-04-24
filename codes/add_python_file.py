"""
@create by Jieqian Chen
@GitHub repository: https://github.com/Jieqian-Chen/Jieqian-Learning-Python
@E-mail: jieqianchen@foxmail.com
@update:
    1. 2020/04/22
    2. 创建 .py 文件时，自动将预定内容写入，简化操作
"""
import os
import datetime
def creat_txt(filename, msg = "Created by: Jieqian-Chen."):
    try:
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                print(msg, file = f)
                f.close()
                print("Creat ok.")
        else:
            print("File exists.")
    except:
        print("Error: creat_txt")

msg1 = """\"\"\"
@create by Jieqian Chen
@GitHub repository: https://github.com/Jieqian-Chen/Jieqian-Learning-Python
@E-mail: jieqianchen@foxmail.com
@update:
    1. """
filename = input("请输入文件名：")
#now = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
msg2 = """{:%Y-%m-%d %H:%M:%S}
\"\"\"
""".format(datetime.datetime.now())
creat_txt(filename, msg1 + msg2)

