#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : insert_sort.py
# Author: ZhouZijian
# Date  : 2018/9/21

"""插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    1、从第一个元素开始，该元素可以认为已经被排序；
    2、取出下一个元素，在已经排序的元素序列中从后向前扫描；
    3、如果该元素（已排序）大于新元素，将该元素移到下一位置；
    4、重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
    5、将新元素插入到该位置后；
    6、重复步骤2~5。
"""
import rdlist


# 插入排序算法实现1
def insert_sort1(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key
    return arr


# 插入排序算法实现2
def insert_sort2(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                i -= 1
                j -= 1
    return arr


# 检测
if __name__ == "__main__":
    print("排序后列表：", insert_sort1(rdlist.rdlist(int(input("输入待检测列表长度：")))))
