# -*- coding:utf-8 -*-
#利用python的短路机制

class Solution:
    def Sum_Solution(self, n):
        # write code here
        self.s=0

        self.add(n)
        return self.s

    def add(self,n):

        self.s = self.s + n
        return n > 0 and self.add(n - 1)