#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : quick_sort.py
# Author: ZhouZijian
# Date  : 2018/9/22

"""快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，
则可分别对这两部分记录继续进行排序，以达到整个序列有序。

快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：
    1、从数列中挑出一个元素，称为 “基准”（pivot）；
    2、重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    3、递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
"""
import rdlist


# 快速排序算法实现
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    l = []
    r = []
    m = arr.pop()
    for i in arr:
        if i > m:
            r.append(i)
        else:
            l.append(i)
    return quick_sort(l) + [m] + quick_sort(r)


# 检测
if __name__ == "__main__":
    print("排序后列表：", quick_sort(rdlist.rdlist(int(input("输入待检测列表长度：")))))
