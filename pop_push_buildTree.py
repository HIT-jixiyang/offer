# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsPopOrder(self, pushV, popV):
        return self.buildTree(pushV, popV)
        # write code here

    def buildTree(self, pushV, popV):

        if len(popV) != len(pushV):
            return False
        if len(popV) == 1 and len(pushV) == 1:
            if pushV[0] == popV[0]:
                return True
            else:
                return False
        if len(popV) == 0:
            return True

        root = pushV[0]
        index = -1
        for i in range(len(popV)):
            if root == popV[i]:
                index = i
        if index < 0:
            return False
        return self.buildTree(pushV[1:index + 1], popV[:index]) and self.buildTree(pushV[i + 1:], popV[i + 1:])
if __name__ == '__main__':

    S=Solution()
    print(S.IsPopOrder([1,2,3,4,5],[5,4,3,2,1]))

