class LinkNode:
    def __init__(self,x):
        self.val=[x]
        self.next=None
def getnode(LinkList):
    while LinkList:
        yield LinkList.val
        LinkList=LinkList.next
if __name__ == '__main__':
    # a=[1,2,3,4,5]
    # b=a
    # a[3]=1
    # print(b)
    # a=[1,1,1,1,1]
    # print(b)
    # l1=LinkNode(1)
    # head=l1
    # l2=LinkNode(2)
    # # l1.val=[2]
    # l1=l2
    # print(head.val)
    # for i in range(2,10):
    #     l1.next=LinkNode(i)
    #     l1=l1.next
    # while head.next:
    #     print(head.val)
    #     head=head.next
    # it=getnode(l2)
    # while True:
    #     try:
    #         print(next(it))
    #     except:
    #         break
    # A=[[0]*10]*10
    # A[0][1]=1
    # print(A)
    A={}
    print(A[0])