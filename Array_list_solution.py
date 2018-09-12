import random


def swap(number_list, index, end):
    temp = number_list[index]
    number_list[index] = number_list[end]
    number_list[end] = temp


def partition(number_list, start, end):
    small = -1
    index = random.randint(start, end - 1)
    swap(number_list, index, end)
    for i in range(start, end):
        if number_list[i] <= number_list[end]:
            small += 1
            if small != i:
                swap(number_list, small, i)
    small += 1
    swap(number_list, small, end)
    return small


def check_more_han_half(number_list, ans):
    count = 0
    mid = len(number_list) >> 1
    for i in number_list:
        if i == ans:
            count += 1
    if count >= mid:
        return True
    return False


def more_than_half_num(number_list):
    if number_list is None or len(number_list) <= 0:
        return -1
    mid = len(number_list) >> 1
    start = 0
    end = len(number_list) - 1
    index = partition(number_list, start, end)
    while index != mid:
        if index > mid:
            end = index - 1
            index = partition(number_list, start, end)
        else:
            start = index + 1
            index = partition(number_list, start, end)
    ans = number_list[mid]
    if not check_more_han_half(number_list, ans):
        return -1
    return ans


def more_than_half_num2(number_list):
    if number_list is None or len(number_list) <= 0:
        return -1
    time = 1
    result = number_list[0]
    for i in range(1, len(number_list)):
        if time == 0:
            result = number_list[i]
            time = 1
        elif number_list[i] == result:
            time += 1
        else:
            time -= 1
    if not check_more_han_half(number_list, result):
        return -1
    return result


def get_least_numbers(number_list, k):
    """
    时间复杂度为O(n),但会改变输入
    :param number_list:
    :param k:
    :return:
    """
    if number_list is None or len(number_list) <= 0:
        return -1
    start = 0
    end = len(number_list) - 1
    index = partition(number_list, start, end)
    ans = []
    while index != k - 1:
        if index > k - 1:
            end = index - 1
            index = partition(number_list, start, end)
        else:
            start = index + 1
            index = partition(number_list, start, end)
    for i in range(k):
        ans.append(number_list[i])
    return ans


def adjust_heap(number_list, i, k):
    pa = i
    child = 2 * i + 1
    temp = number_list[i]
    while child < k:
        if child < k - 1 and number_list[child] < number_list[child + 1]:
            child += 1
        if number_list[pa] >= number_list[child]:
            break
        else:
            number_list[pa] 
    pass


def get_least_numbers2(number_list, k):
    """
    时间复杂度为o(nlogk)适用于处理海量数据，不会改变输入list。最大堆处理方法
    :param number_list:
    :param k:
    :return:
    """
    for i in range(k / 2)[::-1]:
        adjust_heap(number_list, i, k)






if __name__ == '__main__':
    number_list = [1,2,3,2,2,2,5,4,2]
    more_than_half_num2(number_list)