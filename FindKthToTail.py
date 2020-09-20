# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        a=[]
        while head is not None:
            a.append(head)
            head=head.next
        if k>len(a) or k<=0:
            return None
        return a[-k]
