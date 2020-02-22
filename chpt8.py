#! python3
# -*- coding: utf-8 -*-

__author__ = 'CaptShaw'

"""
    chapter 8 mad libs
 
"""
import os, re, shelve, sys
def mad_libs():
    # filename = input('please input a filename')
    filename = 'test.txt'

    with open(filename, 'r') as f:
        content = f.read()
        print(content)

    kwRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    # x = len(kwRegex.findall(content))
    # print(x)
    for i in range(len(kwRegex.findall(content))):
        relp = input('enter an ' + kwRegex.search(content).group())
        content = kwRegex.sub(relp, content, count=1)

    with open(filename, 'w') as f:
        f.write(content)
        print(content)

if __name__ =='__main__':
    mad_libs()
