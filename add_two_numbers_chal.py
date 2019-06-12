"""
Classic two sum challenge
"""


import random
import time


def check_for_sum(num_list, sum):
    check_dict = {}
    for num in num_list:
        num_to_look_for = sum - num
        check_dict[num_to_look_for] = num_to_look_for
        if num in check_dict:
            return True
    return False


if __name__ == '__main__':
    last_num = 1000000
    second_to_last = (last_num - 1)
    sum = last_num + second_to_last

    num_list = []
    num_list.append(second_to_last)
    num_list.extend([num for num in range(second_to_last - 1)])

    start_false_time = time.time()
    false_test = check_for_sum(num_list, sum)
    finish_false_time = time.time()

    start_append_time = time.time()
    num_list.append(last_num)
    finish_append_time = time.time()

    start_true_time = time.time()
    true_test = check_for_sum(num_list, sum)
    finish_true_time = time.time()

    print('Should be false: {}'.format(false_test))
    print('False time completed in {} seconds'.format(finish_false_time - start_false_time))

    print('Append time: {} seconds'.format(finish_append_time - start_append_time))

    print('Should be true: {}'.format(true_test))
    print('True time completed in {} seconds'.format(finish_true_time - start_true_time))
