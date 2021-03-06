#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : bubble_sort.py
# Author: ZhouZijian
# Date  : 2018/9/21

"""冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
    1、比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    3、针对所有的元素重复以上的步骤，除了最后一个；
    4、重复步骤1~3，直到排序完成。
"""
import rdlist


# 冒泡排序算法实现
def bubble_sort(arr):
    count = len(arr)
    for i in range(count):
        for j in range(i+1, count):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# 检测
if __name__ == "__main__":
    print("排序后列表：", bubble_sort(rdlist.rdlist(int(input("输入待检测列表长度：")))))
