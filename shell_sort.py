#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : shell_sort.py
# Author: ZhouZijian
# Date  : 2018/9/24

"""
希尔排序，第一个突破O(n2)的排序算法，是简单插入排序的改进版。它与插入排序的不同之处在于，
它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。

希尔排序先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：
    1、选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
    2、按增量序列个数k，对序列进行k趟排序；
    3、每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m的子序列，分别对各子表进行直接插入排序。
    仅增量因子为1时，整个序列作为一个表来处理，表长度即为整个序列的长度。
"""
import rdlist


# 希尔排序算法实现
def shell_sort(arr):
    count = len(arr)
    gap = count // 2
    # 地板除，取整数
    while gap > 0:
        n = 0
        for i in range(n, count, gap):
            for j in range(i + gap, count, gap):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            n += 1
        gap = gap // 2
    return arr


# 检测
if __name__ == "__main__":
    print("排序后列表：", shell_sort(rdlist.rdlist(int(input("输入待检测列表长度：")))))