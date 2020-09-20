#双栈，使用min栈保存压入时的最小值
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)
    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]
# # -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.m=float('inf')
#         self.stack=[]
#     def push(self, node):
#         # write code here
#         if node<self.m:
#             self.m=node
#         self.stack.append(node)
#     def pop(self):
#         # write code here
#         r=self.stack.pop(-1)
#         self.m=min(self.stack)
#         return r
#     def top(self):
#         # write code here
#         return self.stack[-1]
#     def min(self):
#         # write code here
#         return self.m
if __name__ == '__main__':
    S=Solution()
    S.push(3)
    print(S.min())
    S.push(4)
    print(S.min())
    S.push(2)
    print(S.min())
    S.push(3)
    print(S.min())
    S.pop()
    print(S.min())
    S.pop()
    print(S.min())
    S.pop()
    print(S.min())
    S.push(0)
    print(S.min())

