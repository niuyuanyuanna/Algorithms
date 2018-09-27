def insertion_sort(nums):
    """
    插入排序,时间复杂度为O(n^2)
    :param nums:
    :return:
    """
    if nums is None or len(nums) == 0:
        return nums
    for i in range(1, len(nums)):
        cur_num = nums[i]
        j = i - 1
        while j > 0 and nums[j] <    cur_num:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = cur_num
    return nums


def add_two_list(nums1, nums2):
    '''
    练习题2.1-4 将两个数组中的数字加起来存入新的数组中，完成sum的功能
    :param nums1:
    :param nums2:
    :return:
    '''
    if nums1 is None or len(nums1) == 0:
        return nums2
    if nums2 is None or len(nums2) == 0:
        return nums1

    m = len(nums1)
    n = len(nums2)
    sum_len = max(m, n) + 1
    nums_sum = [0 for i in range(sum_len)]
    carray = 0
    while m > 0 and n > 0:
        temp_sum = nums1[m - 1] + nums2[n - 1] + carray
        if temp_sum / 10 == 0:
            carray = 1
        else:
            carray = 0
        temp_sum %= 10
        nums_sum[sum_len - 1] = temp_sum
        m -= 1
        n -= 1
        sum_len -= 1
    return nums_sum


