#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : rdlist.py
# Author: ZhouZijian
# Date  : 2018/9/21
import random


# 随机生成长度为n的列表，元素为10000以内的自然数
def rdlist(n):
    list = []
    for i in range(n):
        list.append(random.randint(1, 10000))
    print("原始列表为：", list)
    return list
