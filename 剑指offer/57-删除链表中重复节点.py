# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        new_head=ListNode(None)
        t=new_head
        new_head.next=pHead
        last_node = None

        first = 0
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                while  pHead.next and pHead.val == pHead.next.val :
                    pHead = pHead.next

                if pHead:
                    pHead = pHead.next
                    new_head.next = pHead
                else:
                    new_head.next = None
            else:
                if pHead:
                    new_head=new_head.next
                    pHead = pHead.next
                else:
                    new_head.next = None


        if t.next:
            return t.next
        else:
            return None