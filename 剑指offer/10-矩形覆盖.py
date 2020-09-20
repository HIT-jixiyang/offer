# -*- coding:utf-8 -*-
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# 比如n=3时，2*3的矩形块有3种覆盖方法：
# 最后一块是横着和最后一块是竖着，两种情况
class Solution:
    def rectCover(self, number):
        # write code here
        l = [0] * (number + 100)
        l[1] = 1
        l[2] = 2
        l[3] = 3
        if number <= 3:
            return l[number]

        for i in range(3, number + 1):
            l[i] = l[i - 1] + l[i - 2]
        return l[number]

