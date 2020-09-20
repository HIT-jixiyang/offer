# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True

        p1 = pRoot
        p2 = pRoot
        return self.iss(p1, p2)

    def iss(self, p1, p2):
        if (not p1) and (not p2):
            return True
        if p1 and p2:
            if p1.val == p2.val:
                return self.iss(p1.left, p2.right) and self.iss(p1.right, p2.left)
            else:
                return False
        else:
            return False

