#! python3
# -*- coding: utf-8 -*-
import pprint, os

__author__ = 'CaptShaw'

"""
    9.8.2  删除不需要的文件 
"""


def bigFile(dir):
    # list = []
    dict = {}
    for dirpath, dirnames, filenames in os.walk(dir):
        # print('dirpath:', dirpath)
        # for dirname in dirnames:
        #     print('dirname:', dirname)
        for filename in filenames:
            # print('filename:', filename)
            size = os.path.getsize(os.path.join(dirpath, filename))
            # if size >= 1:
            size /= 1024
            if size < 1024:
                size = str(int(size + 1)) + 'KB'
            else:
                size /= 1024
                size = '%.2f' % size + 'MB'
            # list += os.path.join(dirpath, filename), size
            dict[filename] = size

    # for item in list:
    #     print(item)
    for k, v in dict.items():
        print(k, ':', v)


if __name__ == '__main__':
    bigFile(r'C:\Users\Shaw\Pictures')
