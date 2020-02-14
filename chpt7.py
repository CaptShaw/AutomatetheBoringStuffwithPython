#! bin/usr/env
# -*- coding:utf-8 -*-

__author__ = 'CaptShaw'

"""
    chapter 7 regular expression
"""

import re, sys


def pswcheck():
    '''强口令检测 写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
    强口令的 定义是：长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字。
    你可 能需要用多个正则表达式来测试该字符串，以保证它的强度。 '''
    flag = 0
    while flag == 0:
        psw = input('please input your password:')
        pswRegex1 = re.compile(r'[a-zA-Z0-9]{8,}')
        pswRegex2 = re.compile(r'\d+')
        pswRegex3 = re.compile(r'[A-Z]+')
        pswRegex4 = re.compile(r'[a-z]+')
        a1 = pswRegex1.search(psw)
        a2 = pswRegex2.search(psw)
        a3 = pswRegex3.search(psw)
        a4 = pswRegex4.search(psw)
        # print(a1, a2, a3, a4)
        if re.compile(r'[^a-zA-Z0-9]').search(psw) != None:
            print('try another')
            continue
        if (a1 != None) and (a2 != None) and (a3 != None) and (a4 != None):
            b = re.compile(r'(.).*(.)').sub(r'\1******\2', psw)
            print('your password', b, 'is good and strong')
            sys.exit()
        else:
            print('try another')


def main():
    pswcheck()


if __name__ == '__main__':
    main()
