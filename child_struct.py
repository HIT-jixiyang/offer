# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1:
            return False
        if not pRoot2:
            return False
        if self.same(pRoot1,pRoot2):
            return True
        return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)

        # write code here
    def same(self,tree1,tree2):

        if not (tree1 and tree2):
            return False
        if tree1.val!=tree2.val and tree1:
            return False
        if tree1.left==None and tree2.left !=None:
            return False
        if tree1.left!=None and tree2.left ==None:
            return False
        if tree1.right==None and tree2.right !=None:
            return False
        if tree1.right != None and tree2.right == None:
            return False
        if tree1.val==tree2.val and tree1.val=='#':
            return True
        if tree1.val == tree2.val and tree1.val!='#':
            return self.same(tree1.left,tree2.left) and self.same(tree1.right,tree2.right)

if __name__ == '__main__':
    S=Solution()
    n0=TreeNode(8)
    n1=TreeNode(8)
    n2=TreeNode(9)
    n3=TreeNode(2)
    n0.left=n1
    n0.right=n2
    n1.left=n3
    print(S.HasSubtree(n0,n0))