# -*- coding:utf-8 -*-
#如果d[i-1]是负数，那当前最大值不能加上d[i-1]
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_num = array[0]
        dp = [0] * len(array)
        dp[0] = array[0]
        for i in range(1, len(array)):
            if dp[i - 1] < 0:
                dp[i] = array[i]
            else:
                dp[i] = array[i] + dp[i - 1]
            if max_num < dp[i]:
                max_num = dp[i]
        return max_num
