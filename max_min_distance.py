# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Tree:
    def getDis(self, root):
        if root is None:
            return 0
        l_max=r_max=-9999999
        r_min=l_min=99999999
        if root.left:
            l_max=l_min=root.left.val
        l_max_layer=l_min_layer=0
        if root.right:
            r_max=r_min=root.right.val
        r_max_layer=r_min_layer=0
        if root.left:
            l_max,l_min,l_max_layer,l_min_layer=self.lay_travel(root.left)
        if root.right:
            r_max,r_min,r_max_layer,r_min_layer=self.lay_travel(root.right)
        if not root.right:
            _max=max(l_max,root.val)
            _min=min(l_min,root.val)
        if not root.left:
            _max = max(r_max, root.val)
            _min = min(r_min, root.val)
        if root.left and root.right:

            _max=max(l_max,r_max,root.val)
            _min=min(l_min,r_min,root.val)
        min_p=0
        max_p=0
        min_later=max_later=0
        if _max==l_max and root.left is not None:
            max_later=l_max_layer+1
            max_p=0
        if _max == r_max and root.right is not None:
            max_p=1
            max_later = r_max_layer + 1
        if _max == root.val:
            max_later = 0
        if _min == l_min and root.left:
            min_later = l_min_layer + 1
            min_p=0
        if _min == r_min and root.right is not None:
            min_p=1
            min_later = r_min_layer + 1
        if _min == root.val:
            min_later = 0
        if min_p==max_p:
            return abs(min_later-max_later)
        else:
            return abs(min_later+max_later)

        # l_max=self.lay_travel(root.right)
    def lay_travel(self,root):
        _min=_max=root.val
        q=[]
        q.append([root,0])
        max_layer=min_layer=0
        while len(q) > 0:
            t = q[0][0]
            d=q[0][1]
            q=q[1:]
            if t.val>_max:
                _max=t.val
                max_layer=d
            if t.val < _min:
                _min = t.val
                min_layer = d
            # result.append(t.val)
            if t.left is not None:
                q.append([t.left,d+1])
            if t.right is not None:
                q.append([t.right,d+1])
        return _max,_min,max_layer,min_layer
if __name__ == '__main__':
    t1=TreeNode(1)
    t2=TreeNode(2)
    t3=TreeNode(3)
    t4=TreeNode(4)
    t5=TreeNode(5)
    t1.left=t2
    t2.left=t3
    t3.left=t4
    t5.left=t5
    S=Tree()
    print(S.getDis(t1))
