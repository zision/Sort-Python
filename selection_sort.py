#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : selection_sort.py
# Author: ZhouZijian
# Date  : 2018/9/23

"""选择排序，n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。
    1、初始状态：无序区为R[1..n]，有序区为空；
    2、第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。
    该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，
    使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
    3、n-1趟结束，数组有序化了。
"""
import rdlist


# 选择排序算法实现O(n^2)
def selection_sort(arr):
    count = len(arr)
    for i in range(count):
        key = arr[i]
        for j in range(i+1, count):
            if arr[j] < key:
                key = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# 检测
if __name__ == "__main__":
    print("排序后列表：", selection_sort(rdlist.rdlist(int(input("输入待检测列表长度：")))))