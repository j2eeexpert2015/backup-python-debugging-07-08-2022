"""
Given two strings containing only values 0 and 1 you have to
perform the XOR of the two strings and print the resultant value.
"""


def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res = res +'0'
        else:
            res = res + '1'

    return res


s = input()
t = input()
print(strings_xor(s, t))