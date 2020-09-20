class TreeNode():
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None


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
        if (self.flag >= len(s)):
            return None
        root = None
        if (l[self.flag] != '$'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
if __name__ == '__main__':
    a=TreeNode(1)
    b=TreeNode(2)
    c=TreeNode(3)
    d=TreeNode(4)

    a.left=b
    a.right=c
    b.left=d
    S=Solution()
    print(S.Serialize(a))
    print(S.Deserialize(S.Serialize(a)))