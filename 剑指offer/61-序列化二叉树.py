# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    flag = -1

    def Serialize(self, root):
        s = ""
        s = self.recursionSerialize(root, s)
        return s

    def recursionSerialize(self, root, s):
        if (root is None):
            s = '$,'
            return s
        s = str(root.val) + ','
        left = self.recursionSerialize(root.left, s)
        right = self.recursionSerialize(root.right, s)
        s += left + right
        return s

    def Deserialize(self, s):
        self.flag += 1
        l = s.split(',')
        root = None
        if (l[self.flag] != '$'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
if __name__ == '__main__':
    S = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    s=S.Serialize(t1)
    print(s)
    print(S.Deserialize(s))