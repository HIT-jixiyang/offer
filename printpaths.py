# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import copy
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        pass

    def FindPath(self, root, expectNumber):
        # write code here
        stack = []
        path = []

        self.paths = []
        self.ex = expectNumber
        self.preOrder(root, path)

        for i in range(len(self.paths)):
            for j in range(i, len(self.paths)):
                if len(self.paths[i]) < len(self.paths[j]):
                    self.paths[i], self.paths[j] = self.paths[j], self.paths[i]

        return self.paths

    def preOrder(self, root, path):
        p=copy.deepcopy(path)
        p.append(root.val)
        if (not root.left) and (not root.right):
            if sum(p) == self.ex:
                self.paths.append(p)
        if root.left:
            self.preOrder(root.left, p)
        if root.right:
            self.preOrder(root.right, p)
if __name__ == '__main__':
    t1=TreeNode(10)
    t2=TreeNode(5)
    t3=TreeNode(12)
    t4=TreeNode(4)
    t5=TreeNode(7)
    t1.left=t3
    t1.right=t2
    t2.left=t5

    S=Solution()
    print(S.FindPath(t1,22))