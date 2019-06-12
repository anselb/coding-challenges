"""
https://www.careercup.com/question?id=5680043955060736

Output top N positive integer in string comparison order. For example, let's say N=1000, then you need to output in string comparison order as below:
1, 10, 100, 1000, 101, 102, ... 109, 11, 110, ...
"""

def sort_int_strings(n):
    int_strings = [str(num) for num in range(1, n + 1)]
    int_strings.sort()
    return int_strings

if __name__ == '__main__':
    print(sort_int_strings(100))
