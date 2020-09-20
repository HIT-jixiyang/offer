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
            return t

if __name__ == '__main__':
    S=Solution()
    n1=ListNode(1)
    n2=ListNode(2)
    n3=ListNode(2)
    n4=ListNode(3)
    n5=ListNode(4)
    n6=ListNode(4)
    n7=ListNode(5)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    n5.next=n6
    n6.next=n7
    S.deleteDuplication(n1)