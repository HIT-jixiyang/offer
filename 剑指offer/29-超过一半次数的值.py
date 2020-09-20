#用最基本的dict记录次数当然可以，但是有新的思路


# 用preValue记录上一次访问的值，count表明当前值出现的次数，如果下一个值和当前值相同那么count++；
# 如果不同count--，
# 减到0的时候就要更换新的preValue值了，
# 因为如果存在超过数组长度一半的值，那么最后preValue一定会是该值。
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        freq = {}
        for i in range(len(numbers)):
            if numbers[i] in freq.keys():
                freq[numbers[i]] += 1

            else:
                freq[numbers[i]] = 1
            if freq[numbers[i]] > len(numbers) // 2:
                return numbers[i]
        return 0
