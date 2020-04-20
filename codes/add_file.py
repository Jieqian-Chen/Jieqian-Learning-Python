"""
@create by Jieqian Chen
@GitHub repository: https://github.com/Jieqian-Chen/Jieqian-Learning-Python
@E-mail: jieqianchen@foxmail.com
@update:
    1. 2020/04/20, os lib
    2. w, r, rb, wb, a, +
"""
import os

def creat_txt(path, filename, msg = "Created by: Jieqian-Chen."):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(filename):
            with open(path + filename, 'w') as f:
                print(msg, file = f)
                f.close()
                print("Creat ok.")
        else:
            with open(path + filename, 'a') as f:
                print(msg, file = f)
                f.close()
                print("Add ok.")
            print("File exists.")
    except:
        print("Error: creat_txt")

msg = """
这是一个来自 Python 添加的文本
"""
creat_txt("C://CJQ/PythonOut/", "test_no1.txt", msg)
