class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return
        else:
            tmp=root.left
            root.left=root.right
            root.right=tmp
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
if __name__ == '__main__':
    S=Solution()
    root=TreeNode(0)
    n1=TreeNode(1)
    n2=TreeNode(2)
    n3=TreeNode(3)
    n4=TreeNode(4)
    n5=TreeNode(5)
    n6=TreeNode(6)
    root.left=n1
    root.right=n2
    n2.left=n3
    n3.left=n4
    n1.left=n5
    print(S.Mirror(root).val)