#递归写法
#
# public int TreeDepth(TreeNode root) {
#     if(root==null){
#         return 0;
#     }
#     int left=TreeDepth(root.left);
#     int right=TreeDepth(root.right);
#     return Math.max(left,right)+1;
# }
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        self.deep = []
        if not pRoot.left and not pRoot.right:
            return 1
        self.mid_order(pRoot.left, 0)
        self.mid_order(pRoot.right, 0)
        return max(self.deep) + 1

    def mid_order(self, root, d):
        if not root:
            return
        if not root.left and not root.right:
            self.deep.append(d + 1)
        else:
            self.mid_order(root.left, d + 1)
            self.mid_order(root.right, d + 1)

