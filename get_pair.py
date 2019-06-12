"""
Email from subscription of Daily Coding Problems
https://galaiko.rocks/posts/2018-07-06/

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b): def pair(f): return f(a, b) return pair Implement car and cdr.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def get_left(left, right):
        return left

    return pair(get_left)


def cdr(pair):
    def get_right(left, right):
        return right

    return pair(get_right)


if __name__ == '__main__':
    left = 332
    right = 1234
    after_cons = cons(left, right)

    left_result = car(after_cons)
    right_result = cdr(after_cons)
    print('Left should be {}: {}'.format(left, left_result))
    print('Right should be {}: {}'.format(right, right_result))
