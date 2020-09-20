# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
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