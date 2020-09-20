# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        a = []
        a.append(0)
        a.append(1)
        a.append(2)
        for i in range(3, number + 1):
            a.append(a[i - 1] + a[i - 2])
        return a[number]
if __name__ == '__main__':
    S=Solution()
    print(S.jumpFloor(4))