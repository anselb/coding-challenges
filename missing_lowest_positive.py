"""
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the smallest missing positive integer.
"""

import time


def first_missing_bad(num_list):
    lowest_missing = 1
    for num in num_list:
        for num in num_list:
            if lowest_missing == num:
                lowest_missing += 1
                break
    return lowest_missing


def first_missing(num_list):
    num_dict = {}
    for num in num_list:
        num_dict[num] = num

    lowest_missing = 1
    for num in num_list:
        if lowest_missing in num_dict:
            lowest_missing += 1

    return lowest_missing


if __name__ == '__main__':
    # test to see if functions works
    # num_list = [3, 4, -1, 1, 5]
    # start = time.time()
    # result = first_missing(num_list)
    # finish = time.time()
    # print('Should be 2: {} in {} seconds'.format(result, finish - start))

    # num_list will be numbers 1000 to 0 [100, 99, 98, ... , 1, 0]
    num_list = [x for x in range(1000, -1, -1)]
    start = time.time()
    result = first_missing_bad(num_list)
    finish = time.time()
    bad_time = finish - start
    print('Should be 1001: {} in {} seconds'.format(result, bad_time))

    num_list = [x for x in range(1000, -1, -1)]
    start = time.time()
    result = first_missing(num_list)
    finish = time.time()
    good_time = finish - start
    print('Should be 1001: {} in {} seconds'.format(result, good_time))
