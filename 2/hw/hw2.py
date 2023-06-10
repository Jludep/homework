"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
import collections

from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    dic = dict(collections.Counter(inp))
    major_ind = max(dic.values())
    minor_ind = min(dic.values())
    major_elem = list(dic.keys())[list(dic.values()).index(major_ind)]
    minor_elem = list(dic.keys())[list(dic.values()).index(minor_ind)]
    return [major_elem, minor_elem]


res=major_and_minor_elem([2,2,1,1,1,2,2])
print(res)