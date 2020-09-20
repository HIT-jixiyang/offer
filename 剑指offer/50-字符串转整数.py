# -*- coding:utf-8 -*-
from functools import reduce
def chr2int(ch):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return d[ch]


def str2int(f, i):
    return f * 10 + i


class Solution:
    def StrToInt(self, s):
        # write code here
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        if not s:
            return 0
        if len(s) == 1:
            if s in d.keys():
                return d[s]
            else:
                return 0

        for i in range(len(s)):
            if not s[i] in d.keys():
                if not (s[i] == '+' or s[i] == '-'):
                    return 0
                if (s[i] == '+' or s[i] == '-') and i != 0:
                    return 0
        if s[0] == '+':
            r = reduce(str2int, map(chr2int, s[1:]))
            if r > 2 ** 31 - 1:
                return 0
            else:
                return reduce(str2int, map(chr2int, s[1:]))
        elif s[0] in d.keys():
            r = reduce(str2int, map(chr2int, s))
            if r > 2 ** 31 - 1:
                return 0
            return r
        else:
            r = -reduce(str2int, map(chr2int, s[1:]))
            if r < -(2 ** 31):
                return 0
            return -reduce(str2int, map(chr2int, s[1:]))
