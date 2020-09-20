class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        result = []
        q = []
        if not root:
            return []

        q.append(root)
        while len(q) > 0:
            t = q[0]
            q = q[1:]
            result.append(t.val)
            if t.left is not None:
                q.append(t.left)
            if t.right is not None:
                q.append(t.right)

        return result