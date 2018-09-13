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


def longest_subString_without_duplication(str):
    str_list = list(str)
    position_list = [-1] * 26
    current_length = 0
    max_length = current_length

    for i in range(0, len(str_list)):
        position_i = position_list[ord(str_list[i]) - ord('a')]
        if position_i == -1 or i - position_i > current_length:
            current_length += 1
        else:
            current_length = i - position_i
        position_list[ord(str_list[i]) - ord('a')] = i
        if current_length > max_length:
            max_length = current_length
    return max_length


if __name__ == '__main__':
    str = 'arabcacfr'
    longest_subString_without_duplication(str)