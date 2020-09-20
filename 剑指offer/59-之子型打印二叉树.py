class Solution:
    def Print(self, pRoot):
        # write code here
        root=pRoot
        if not root:
            return []
        level=[root]
        result=[]
        lefttoright=False
        while level:
            curvalues=[]
            nextlevel=[]
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if lefttoright:
                curvalues.reverse()
            if curvalues:
                result.append(curvalues)
            level=nextlevel
            lefttoright=not lefttoright
        return result
