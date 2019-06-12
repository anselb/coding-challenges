"""
https://www.careercup.com/question?id=5684278553739264

Output top N positive integer in string comparison order. For example, let's say N=1000, then you need to output in string comparison order as below:
1, 10, 100, 1000, 101, 102, ... 109, 11, 110, ...
"""

def unique_char_substring(str):
    if len(str) < 2:
        return str

    left_ind = 0
    right_ind = 0
    longest = str[0]
    char_set = set(longest)

    for char_ind in range(1, len(str)):
        character = str[char_ind]
        # print("on char: ", character)

        if character not in char_set:
            char_set.add(character)
            right_ind += 1
        # If both ends are the same shift splice window by 1
        elif character == str[left_ind]:
            right_ind += 1
            left_ind += 1
        # If ends are not the same, make them the same and shift window by 1
        else:
            while str[left_ind] != character:
                char_set.remove(str[left_ind])
                left_ind += 1
            right_ind += 1
            left_ind += 1

        # print(str[left_ind:right_ind + 1])
        # print(char_set)
        if right_ind - left_ind > len(longest) - 1:
            longest = str[left_ind:right_ind + 1]

    return longest

if __name__ == '__main__':
    print(unique_char_substring("awbacgabcjqba"))
    # gabcjq
    print(unique_char_substring("awbacgabbcjqba"))
    # wbacg
