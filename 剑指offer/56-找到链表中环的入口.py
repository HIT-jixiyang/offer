# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#还有一种方法是使用快慢指针，快指针跑得快一定能追上慢指针

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        d={}
        while pHead:
            if id(pHead) in d.keys():
                return pHead
            d[id(pHead)]=1
            pHead=pHead.next
        return None