# class Solution:
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         if not pHead or not pHead.next:
#             return pHead
#         h=None
#         while pHead:
#             tmp=pHead
#             pHead=pHead.next
#             tmp.next=h
#             h=tmp
#         return h
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 递归方法
    def ReverseList(self, pHead):
        if (not pHead) or (not pHead.next):
            return pHead
        re_node=self.ReverseList(pHead.next)
        pHead.next.next=pHead
        pHead.next=None
        return re_node
if __name__ == '__main__':
    S=Solution()
    n_1=ListNode(1)
    n_2=ListNode(2)
    n_3=ListNode(3)
    n_4=ListNode(4)
    n_1.next=n_2
    n_2.next=n_3
    n_3.next=n_4
    print(S.ReverseList(n_1))




