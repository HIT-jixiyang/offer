# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.array = []
    def KthNode(self, pRoot, k):
        if k<=0:
            return None
        self.mid_travel(pRoot)
        if len(self.array)<k:
            return None
        return self.array[k-1]
    def mid_travel(self,pRoot):
        if pRoot is None:
            return
        self.mid_travel(pRoot.left)
        self.array.append(pRoot)
        self.mid_travel(pRoot.right)
if __name__ == '__main__':
    S=Solution()
    t1=TreeNode(10)
    t2=TreeNode(8)
    t3=TreeNode(5)
    t4=TreeNode(6)
    t5=TreeNode(7)
    t6=TreeNode(9)
    t7=TreeNode(11)
    t1.left=t2
    t2.left=t4
    t2.right=t6
    t1.right=t7
    t4.left=t3
    t6.right=t5
    # t5.right=t8
    print(S.KthNode(t1,7).val)
    print(S.array)
