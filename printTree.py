# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        Q = []
        Q.append([pRoot, 0])
        i = 0
        while len(Q)>0:
            t = Q[0]
            Q = Q[1:]
            if i < t[1]:
                print('\n')
                i = t[1]
            print(t[0].val,end='')
            if t[0].left is not None:
                Q.append([t[0].left, t[1] + 1])
            if t[0].right is not None:
                Q.append([t[0].right, t[1] + 1])
if __name__ == '__main__':
    S=Solution()
    t1=TreeNode(8)
    t2=TreeNode(6)
    t3=TreeNode(10)
    t4=TreeNode(5)
    t5=TreeNode(7)
    t6=TreeNode(9)
    t7=TreeNode(11)
    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    t3.left=t6
    t3.right=t7
    S.Print(t1)

        # write code here