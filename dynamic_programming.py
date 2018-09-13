#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/11 18:09
# @Author  : NYY
# @Site    : www.niuyuanyuanna.git.io
# @File    : dynamic_programming.py
import numpy as np


def cutRod_BottomUp_withCost(price_list, length, cost):
    """
    自底向上实现钢材切割，并添加每次切割的成本
    :param price_list:
    :param length:
    :param cost:
    :return:
    """
    if length < 0 or length >= len(price_list):
        return 0
    r = [0] * len(price_list)

    # i表示钢材长度为i时，自底向上计算
    for i in range(length):
        q = 0
        # j表示前面一半钢材的长度固定为j时，查找后一半钢材长度的最优切割方法
        for j in range(1, i + 1):
            if i == j:
                temp = price_list[j]
            else:
                temp = price_list[j] + r[i - j] - cost

            if temp > q:
                q = temp
                r[i] = temp
    return r


def memoized_cut_aux(price_list, n, r, s):
    """
    自顶向下切割，需要使用一个list存放之前已经计算过的结果
    :param price_list: 价格表
    :param n: 钢材长度
    :param r: 最优解list
    :return: n对应的最佳解
    """
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            temp = price_list[i] + memoized_cut_aux(price_list, n - i, r, s)
            if temp > q:
                q = temp
                s[i] = n - i
                r[i] = q
    return q


def memoized_cut_rod(price_list, length):
    r = [-1] * (length + 1)
    s = [-1] * (length + 1)
    return memoized_cut_aux(price_list, length, r, s)


def fibnacci_func(n):
    if n <= 1:
        return n
    one = 0
    two = 1
    result = 0
    for i in range(2, n + 1):
        result = one + two
        one = two
        two = result
    return result


def longest_commom_subsequence(X, Y):
    """
    最长公共子序列，采用自底而上的方法，使用两个mn空间复杂度的matrix存储每个转移状态
    :param X:
    :param Y:
    :return:
    """
    m = len(X) + 1
    n = len(Y) + 1
    c = np.zeros((m, n))
    b = np.zeros((m - 1, n - 1))
    X.insert(0, '0')
    Y.insert(0, '0')
    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                c[i, j] = 1 + c[i - 1, j - 1]
                b[i - 1, j - 1] = 1
            elif c[i - 1, j] >= c[i, j - 1]:
                c[i, j] = c[i - 1, j]
                b[i - 1, j - 1] = 2
            else:
                c[i, j] = c[i, j - 1]
                b[i - 1, j - 1] = 3
    return c, b


def print_LCS(b, X, i, j):
    """
    根据存储的b打印出最长子序列
    :param b: 最长子序列的路线
    :param X:
    :param i:
    :param j:
    :return:
    """
    if i == 0 or j == 0:
        return 0
    if b[i][j] == 1:
        print_LCS(b, X, i - 1, j - 1)
        print(X[i])
    elif b[i][j] == 2:
        print_LCS(b, X, i - 1, j)
    else:
        print_LCS(b, X, i, j - 1)


if __name__ == '__main__':
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']
    c, b = longest_commom_subsequence(X, Y)
    print_LCS(b, X, len(X), len(Y))
