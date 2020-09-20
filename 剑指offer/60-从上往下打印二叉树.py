# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        q=[]
        level=0
        q.append([pRoot,level])
        result=[]
        last_level=0
        layer=[]
        while len(q)>0:

            [t,t_level]=q.pop(0)
            if t_level!=last_level:
                result.append(layer)
                layer=[t.val]
                last_level=t_level
            else:
                layer.append(t.val)
                last_level=t_level
            if t.left:
                q.append([t.left,t_level+1])
            if t.right:
                q.append([t.right,t_level+1])
        if len(layer)>0:
            result.append(layer)
        return result
if __name__ == '__main__':
    S=Solution()
    t1=TreeNode(1)
    t2=TreeNode(2)
    t3=TreeNode(3)
    t4=TreeNode(4)
    t5=TreeNode(5)
    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    print(S.Print(t1))