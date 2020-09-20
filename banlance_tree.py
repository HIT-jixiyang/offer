# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.deep = {}
        self.getDeep(pRoot)
        return self.isBan(pRoot)

    def isBan(self, root):

        if not root:
            return True
        if not root.left and root.right:
            if self.deep[hash(root.right)]>=2:
                return False
            return True
        if not root.right and root.left:
            if self.deep[hash(root.left)]>=2:
                return False
            return True
        if not root.right and not root.left:
            return True

        if root.left and root.right:
            A=self.isBan(root.left)
            B=self.isBan(root.right)
            c=abs(self.deep[hash(root.left)] - self.deep[hash(root.right)]) <= 1
            return  A and B and c

    def getDeep(self, root):
        if not root:
            self.deep[hash(root)] = 0
        elif not root.left and not root.left:
            self.deep[hash(root)] = 1
        else:
            self.getDeep(root.left)
            self.getDeep(root.right)
            self.deep[hash(root)] = max(self.deep[hash(root.left)], self.deep[hash(root.right)]) + 1




if __name__ == '__main__':
    t1=TreeNode(1)
    t2=TreeNode(2)
    t3=TreeNode(3)
    t4=TreeNode(4)
    t1.left=t2
    t2.left=t3
    t1.right=t4
    S=Solution()
    print(S.IsBalanced_Solution(t1))
