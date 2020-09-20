
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root,float('-inf'),float('inf'))
    def isValid(self,root,low,up):
        if not root:
            return True
        val=root.val
        if val<=low or val>=up:
            return False

        return self.isValid(root.left,low,val) and self.isValid(root.right,val,up)


