#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/11 18:09
# @Author  : NYY
# @Site    : www.niuyuanyuanna.git.io
# @File    : dynamic_programming.py


def cutRod_BottomUp_withCost(price_list, length, cost):
    if length < 0 or length >= len(price_list):
        return 0
    r = [0] * len(price_list)

    # i表示钢材长度为i时，自底向上计算
    for i in range(length):
        q = 0
        # j表示前面一半钢材的长度固定为j时，查找后一半钢材长度的最优切割方法
        for j in range(1, i+1):
            if i == j:
                temp = price_list[j]
            else:
                temp = price_list[j] + r[i - j] - cost

            if temp > q:
                q = temp
                r[i] = temp
    return r


if __name__ == '__main__':
    price_list = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    cost = 1
    print(cutRod_BottomUp_withCost(price_list, 9, cost))