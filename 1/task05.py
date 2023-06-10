"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k > 1 and k <= len(nums):    #Function for checking the size of a new subarray
        result = max(nums)
        for len_subnums in range(0, k):
            for n in range(0,(len(nums) - len_subnums + 1)):
                if result < sum(nums[n:n + len_subnums + 1]): #The function of finding the sum of the values of the subarray
                    result = sum(nums[n:n + len_subnums + 1])
        return result
    else:
        return False

find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3)
