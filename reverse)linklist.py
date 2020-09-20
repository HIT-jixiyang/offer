import copy
class LinkListNode:
    val=None
    def __init__(self,v):
        self.next=None
        self.val=v
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        h=None
        while pHead:
            tmp=pHead
            pHead=pHead.next
            tmp.next=h
            h=tmp
        return h
if __name__ == '__main__':
    n1=LinkListNode(1)
    n2=LinkListNode(2)
    n3=LinkListNode(3)
    n4=LinkListNode(4)
    n5=LinkListNode(5)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    S=Solution()
    p=S.ReverseList(n1)
    print(p.val)
    pass

