#! python3
# -*- coding: utf-8 -*-

__author__ = 'CaptShaw'

"""
     选择性拷贝 编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg）。不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中。 
    copy file considering format such as .pdf .jpg
"""

import os, shutil


def copyFormat(format, dst='', src=os.path.abspath('.')):
    ''' format e.g. jpg pdf
        dir defalt value is parent work directory'''
    file_list = []

    os.mkdir(dst)
    for dirpath, dirnames, filenames in os.walk(src):
        print('current path is:', dirpath)
        for dirname in dirnames:
            print('dirname is:', dirname)
        for filename in filenames:
            print('filename is:', filename)
            if os.path.splitext(filename)[1] == '.' + format:
                if not os.path.exists(os.path.join(dst, filename)):
                    shutil.copy(os.path.join(dirpath, filename), dst)
                else:
                    shutil.copy(os.path.join(dirpath, filename), os.path.join(dst, filename + '(1)'))

    print(dst)


if __name__ == '__main__':
    copyFormat('png', r'C:\Users\Shaw\Pictures\new', r'C:\Users\Shaw\Pictures')
