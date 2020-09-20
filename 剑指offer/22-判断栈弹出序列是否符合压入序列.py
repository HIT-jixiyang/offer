# -*- coding:utf-8 -*-
#一是利用中序和先序构造二叉树
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
        return self.buildTree(pushV[1:index + 1], popV[:index]) and self.buildTree(pushV[index + 1:], popV[index + 1:])

#暴力方法
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or len(pushV) != len(popV):
            return 0
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        if len(stack):
            return 0
        return 1