#! python3
# -*- coding: utf-8 -*-
import os
import re
import shutil

__author__ = 'CaptShaw'

"""
    9.8.3  消除缺失的编号 编写一个程序，在一个文件夹中，
    找到所有带指定前缀的文件，诸如 spam001.txt, spam002.txt 等，
    并定位缺失的编号（例如存在 spam001.txt 和 spam003.txt，但不存 在 spam002.txt）。
    让该程序对所有后面的文件改名，消除缺失的编号。 
    作为附加的挑战，编写另一个程序，
    在一些连续编号的文件中，空出一些编号， 以便加入新的文件。 
 
"""


def order_keeper(prefix, dir='.'):
    if os.path.isdir(dir):
        pass
    else:
        raise Exception('unacceptalbe dir')
        exit('unacceptalbe dir')
    # print(prefix)
    container = []
    os.chdir(dir)
    l = len(prefix)
    num_list = []
    for filename in os.listdir():
        if prefix not in filename:
            continue
        name, ext = os.path.splitext(filename)
        num = re.compile(r'^' + prefix + r'[0]*(\d{1,3})').search(name).group(1)
        num_list += [int(num)]
        container += [[prefix, '%03d' % int(num), ext]]

    # print(container)
    # print(num_list)

    for i in range(1, len(num_list)):
        if num_list[i] - num_list[i - 1] > 1:
            num_list[i] = num_list[i - 1] + 1
        new_num = '%03d' % num_list[i]
        # print(container)
        # print(num_list)
        new_name = ''.join([prefix, new_num, container[i][2]])
        # print(os.path.join(dir,''.join(container[i][:])),os.path.join(dir,new_name))
        shutil.move(os.path.join(dir, ''.join(container[i][:])), os.path.join(dir, new_name))
        print('renaming ' + os.path.join(dir, ''.join(container[i][:])) + ' as ' + os.path.join(dir, new_name))


if __name__ == '__main__':
    try:
        order_keeper('spam', r'C:\Users\Shaw\PycharmProjects\exercise\test')
    except Exception as err:
        print('an error happened:' + str(err))
