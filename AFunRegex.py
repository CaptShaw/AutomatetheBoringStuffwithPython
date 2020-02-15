#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint

__author__ = 'CaptShaw'

"""
    saw a fun regular expression in a case of Chinese
"""
import re

text = '牧牌全脂牛奶1L*12盒【品牌】： 牧牌【规格】：1L*12盒（乳脂肪含量≥3.5%）【产地】：德国【类型】：超高温瞬时灭菌纯牛奶【原料】：100%牛奶【非脂乳固体含量】：≥8.5%【生产日期】：见包装【保质期】：12个月储藏条件 置于阴凉干燥处存放食用方法使用前摇匀。开启后，请储藏于1-4℃，并于3日内饮用完。'
# demand 提取出【】内的文字和对应的内容'

# TODO titleRegex
# titleRegex = re.compile(r'【\w+】：')
titleRegex = re.compile(r'【(\w+)】')  # 重要细节变化
# TODO contentRegex
# contentRegex = re.compile(r'：[^：【】]+[【。]')
contentRegex = re.compile(r'：([^：【】]+)[【。]')  # 重要细节变化
# TODO put it togather
t = titleRegex.findall(text)
c = contentRegex.findall(text)
print(t)
print(c)
pprint.pprint(dict(zip(t, c)))
