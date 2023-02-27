import os
import sys


def get_par_path():
    root_path = os.path.abspath(os.path.dirname(__file__)).split('Utils')[0]
# 返回的就是根路径
    return root_path

# a=root_path = os.path.abspath(os.path.dirname(__file__)).split('Utils')[0]
# print(a)
# sys.path.append('..')
# driver_path = os.path.join(get_par_path(),"driver\\chromdriver.exe")
# print(driver_path)