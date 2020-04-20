"""
@create by Jieqian Chen
@GitHub repository: https://github.com/Jieqian-Chen/Jieqian-Learning-Python
@E-mail: jieqianchen@foxmail.com
@update:
    1. 2020/04/20, os lib
    2. w, r, rb, wb, a, +
"""
import os

def creat_txt(path, filename):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(filename):
            with open(path + filename, 'a') as f:
                print("Created by: Jieqian-Chen.", file = f)
                f.close()
                print("Creat ok.")
        else:
            print("File exists.")
    except:
        print("Error: creat_txt")

creat_txt("F://00CJQtest/", "test_no1.txt")
