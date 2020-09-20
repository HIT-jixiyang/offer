# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if not head.next or not head:
            return head
        n1 = head
        n2 = head.next
        last = ListNode(None)
        r = last
        while n1 and n2:
            n1.next = n2.next
            n2.next = n1
            last.next = n2
            last = n1
            n1 = n1.next
            n2 = n1.next
        return r.next

if __name__ == '__main__':
    l1=ListNode(1)
    l2=ListNode(2)
    l3=ListNode(3)
    l4=ListNode(4)
    l1.next=l2
    l2.next=l3
    l3.next=l4
    S=Solution()
    S.swapPairs(l1)