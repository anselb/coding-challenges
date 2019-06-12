"""
https://www.careercup.com/question?id=16306671

You are given an integer array, where all numbers except for TWO numbers appear even number of times.

Q: Find out the two numbers which appear odd number of times.
"""

import unittest
ut = unittest.TestCase('__init__')

def count_nums(int_list):
    count_dict = {}
    for int in int_list:
        if int not in count_dict:
            count_dict[int] = True
        else:
            count_dict[int] = not count_dict[int]

    odd_nums = []
    for int in count_dict:
        if count_dict[int] == True:
            odd_nums.append(int)

    return odd_nums

if __name__ == '__main__':
    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    ut.assertListEqual(count_nums(list1), [2, 5])

    list2 = [1, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 3]
    ut.assertListEqual(count_nums(list2), [1, 3])
