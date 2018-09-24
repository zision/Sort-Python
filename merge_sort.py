#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : merge_sort.py
# Author: ZhouZijian
# Date  : 2018/9/24

"""归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，
再合并数组。将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组
的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个
数组为空，最后把另一个数组的剩余部分复制过来即可。
"""
import rdlist


# 归并排序算法实现
def merge_sort(arr):
    count = len(arr)
    if count <= 1:
        return arr
    else:
        num = len(arr) // 2
        left = merge_sort(arr[:num])
        right = merge_sort(arr[num:])
    # 中间过程测试
    # print("left:%s" % left)
    # print("right:%s" % right)
    cache_list = []
    l_num, r_num = 0, 0
    while l_num < len(left) and r_num < len(right):
        if left[l_num] < right[r_num]:
            cache_list.append(left[l_num])
            l_num += 1
        else:
            cache_list.append(right[r_num])
            r_num += 1
    cache_list += left[l_num:]
    cache_list += right[r_num:]
    return cache_list


# 检测
if __name__ == "__main__":
    print("排序后列表：", merge_sort(rdlist.rdlist(int(input("输入待检测列表长度：")))))
