# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#获得长度差d，然后让长的先走d步，然后长短一起走，第一个相同节点就是答案
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        p1_len = 0
        p2_len = 0
        while p1:
            p1_len += 1
            p1 = p1.next
        while p2:
            p2_len += 1
            p2 = p2.next
        if p1_len >= p2_len:
            d = p1_len - p2_len
            for i in range(d):
                pHead1 = pHead1.next
            while pHead1:
                if pHead1 is pHead2:
                    return pHead1
                else:
                    pHead1 = pHead1.next
                    pHead2 = pHead2.next
        else:
            d = p2_len - p1_len
            for i in range(d):
                pHead2 = pHead2.next
            while pHead1:
                if pHead1 is pHead2:
                    return pHead1
                else:
                    pHead1 = pHead1.next
                    pHead2 = pHead2.next
        return None


