# 用一个大顶堆，保存当前滑动窗口中的数据。滑动窗口每次移动一格，就将前面一个数出堆，后面一个数入堆。
#当然python直接暴力求解也行吧
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        if size<=0:
            return []
        if size>len(num):
            return []
        result=[]
        for i in range(0,len(num)-size+1):
            win=num[i:i+size]
            result.append(max(win))
        return result
        # write code here
