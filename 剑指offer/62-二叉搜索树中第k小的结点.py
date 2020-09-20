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