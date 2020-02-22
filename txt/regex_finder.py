#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'CaptShaw'

"""
    chapter 8.9.3 正则表达式查找
    编写一个程序，打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达式的所有行。结果应该打印到屏幕上。 
    regex_finder
"""

import os, re

def cutter():
    # to cut ccp.txt apart
    #http://www.12371.cn/special/zggcdzc/zggcdzcqw/
    with open('ccp.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()

    titleRegex = re.compile('总.*纲|第.{1,2}章.*')
    order = []
    for line in content:
        if titleRegex.search(line) != None:
            order += [content.index(line)]

    for o in range(len(order)):
        if o < len(order) - 1 :
            chapter = content[order[o]:order[o+1]]
        elif o == len(order) - 1 :
            chapter = content[order[o]:]
        # title = re.compile('\s').sub('',str(content[order[o]]))
        # title = str(content[order[o]]).strip()
        title = str(content[order[o]].strip()) + '.txt'
        with open(title, 'w+', encoding='utf-8') as f:
            f.write(''.join(chapter))

def regex_finder(regex):
    # txt file all together
    ls_txt = []
    for item in os.listdir():
        item = str(item).split('.')
        if len(item) > 1 and item[1] == 'txt':
            ls_txt.append('.'.join(item))
    # print(ls_txt)
    Regex = re.compile(regex)
    num = 0
    for file in ls_txt:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        for line in content:
            match = Regex.search(line)
            if match != None:
                print(line)
                num += 1
    print('共计',num,'条')

if __name__ == '__main__':
    cutter()
    # regex = input('please input a regex: ')
    # regex = r'第.*条'
    # regex_finder(regex)




