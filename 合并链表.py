# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead2:
            return pHead1
        if not pHead1:
            return pHead2
        if pHead1.val>pHead2.val:
            p=pHead2
            new_head=pHead2
            pHead2=pHead2.next
            while pHead1 and pHead2:
                if pHead1.val>pHead2.val:
                    p.next=pHead2
                    p=p.next
                    pHead2 = pHead2.next
                else:
                    p.next=pHead1
                    p=p.next
                    pHead1=pHead1.next
            while pHead1:
                p.next=pHead1
                p=p.next
                pHead1 = pHead1.next
            while pHead2:
                p.next = pHead2
                p = p.next
                pHead2 = pHead2.next

        else:
            p = pHead1
            new_head = pHead1
            pHead1 = pHead1.next
            while pHead1 and pHead2:
                if pHead1.val > pHead2.val:
                    p.next = pHead2
                    p = p.next
                    pHead2=pHead2.next
                else:
                    p.next = pHead1
                    p = p.next
                    pHead1=pHead1.next
            while pHead1:
                p.next = pHead1
                p = p.next
                pHead1=pHead1.next
            while pHead2:
                p.next = pHead2
                p = p.next
                pHead2=pHead2.next
        return new_head
def print_list(List):
    while List:
        print(List.val)
        List=List.next
if __name__ == '__main__':
    S=Solution()
    l1=ListNode(0)
    l2=ListNode(1)
    l3=ListNode(3)
    l4 = ListNode(2)
    l5= ListNode(4)
    l6= ListNode(5)
    l1.next=l2
    l2.next=l3
    l4.next=l5
    l5.next=l6
    p=S.Merge(l1,None)
    print_list(p)
