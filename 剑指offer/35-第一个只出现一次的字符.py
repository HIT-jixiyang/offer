#利用list.count
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        count = {}
        first_appear = {}
        for i in range(len(s)):
            if s[i] in count.keys():

                count[s[i]] += 1
            else:
                count[s[i]] = 1
            if count[s[i]] == 1:
                first_appear[s[i]] = i
        min_appear = 9999999
        for key in count.keys():
            if count[key] == 1 and min_appear > first_appear[key]:
                min_appear = first_appear[key]
        if min_appear == 9999999:
            return -1
        return min_appear