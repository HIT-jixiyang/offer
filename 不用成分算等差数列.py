# -*- coding:utf-8 -*-

class Solution:
    def Sum_Solution(self, n):
        # write code here
        self.s=0

        self.add(n)
        return self.s

    def add(self,n):

        self.s = self.s + n
        return n > 0 and self.add(n - 1)
if __name__ == '__main__':
    S=Solution()
    print(S.Sum_Solution(5))
