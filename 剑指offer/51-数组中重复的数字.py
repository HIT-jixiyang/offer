# -*- coding:utf-8 -*-
#排序后返回第一个重复的

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        numbers=sorted(numbers)
        for i in range(1,len(numbers)):
            if numbers[i]==numbers[i-1]:
                duplication[0]=numbers[i]
                return True
        return False