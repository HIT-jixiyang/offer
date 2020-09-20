# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s)==0:
            return ''
        return s[n%len(s):]+s[:n%len(s)]