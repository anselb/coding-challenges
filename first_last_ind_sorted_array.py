"""
Given a sorted array, find the index of the first
and last occurrence of a given element. If the given
element is not found in the array, report that.
"""


def first_last_ind(arr, num):
    left_ind = binary_search(arr, num)
    right_ind = left_ind

    if left_ind == None:
        return ()

    while left_ind > 0 and arr[left_ind - 1] == num:
        left_ind -= 1
    while right_ind < len(arr) - 1 and arr[right_ind + 1] == num:
        right_ind += 1

    return (left_ind, right_ind)


def binary_search(arr, item):
    left = 0
    right = len(arr) - 1
    # Has to be just less than
    while left < right:
        mid_ind = (left + right) // 2
        if arr[mid_ind] == item:
            return mid_ind
        elif arr[mid_ind] > item:
            # Cannot be +1
            right = mid_ind
        elif arr[mid_ind] < item:
            # Has to be +1
            left = mid_ind + 1

    return None


if __name__ == '__main__':
    # Inds:  0  1  2  3  4  5  6  7  8  9  10
    list1 = [1, 1, 1, 2, 3, 3, 3, 3, 5, 5, 5]
    print(first_last_ind(list1, 1))  # (0, 2)
    print(first_last_ind(list1, 2))  # (3, 3)
    print(first_last_ind(list1, 3))  # (4, 7)
    print(first_last_ind(list1, 4))  # ()
    print(first_last_ind(list1, 5))  # (8, 10)
