# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        pass
    def push(self, node):
        self.stack1.append(node)
        # write code here
    def pop(self):
        if len(self.stack2)==0:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop(-1))
        if len(self.stack2)>0:
            return  self.stack2.pop(-1)
        else:
            return None
        # return xx
if __name__ == '__main__':
    S=Solution()
    S.push(1)
    S.push(2)
    S.push(3)
    print(S.pop())
    # S.pop()
    print(S.pop())
    S.push(4)
    print(S.pop())
    S.push(5)
    print(S.pop())
    print(S.pop())
    # S.pop()
    # S.pop()