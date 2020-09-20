# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p = head
        q = head
        list1 = ListNode(1)
        list2 = ListNode(2)
        l1 = list1
        l2 = list2
        # while p is not None:
        #     if p.val>=x:
        #         list1=p
        #         break
        #     p=p.next

        # while q is not None:
        #     if q.val<x:
        #         list2=q
        #         break
        #     q=q.next
        while head is not None:
            if head.val >= x:
                list2.next = head
                list2 = list2.next
            else:
                list1.next = head
                list1 = list1.next
            head = head.next
        list2.next=None
        list1.next = l2.next
        return l1.next


if __name__ == '__main__':
    S=Solution()
    l1=ListNode(3)
    l2=ListNode(5)
    l3=ListNode(8)
    l4=ListNode(5)
    l5=ListNode(10)
    l6=ListNode(2)
    l7=ListNode(1)
    l1.next=l2
    l2.next=l3
    l3.next=l4
    l4.next=l5
    l5.next=l6
    l6.next=l7
    S.partition(l1,5)