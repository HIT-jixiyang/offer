# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        mid_order=sorted(preorder)
        print(mid_order)
        print(preorder)
        Tree=self.buildTree(mid_order,preorder)
        self.mid_travel(Tree)
    def buildTree(self,mid_order,preorder):
        if len(mid_order)>0 and len(preorder)>0:
            t=TreeNode(preorder[0])
            for i in range(len(mid_order)):
                if mid_order[i]==t.val:
                    break
            t.left=self.buildTree(mid_order[:i],preorder[1:i+1])
            t.right=self.buildTree(mid_order[i+1:],preorder[i+1:])
        else:
            return None
        return t
    def mid_travel(self,t):
        if t is None:
            return
        if t.left is not None:
            self.mid_travel(t.left)
        print(t.val)
        if t.right is not None:
            self.mid_travel(t.right)
if __name__ == '__main__':
    S=Solution()
    S.bstFromPreorder([8,5,1,7,10,12])