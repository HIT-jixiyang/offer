# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a=[]
        a.append(0)
        a.append(1)
        for i in range(2,n+1):
            a.append(a[i-1]+a[i-2])
        return a[n]
if __name__ == '__main__':
    S=Solution()
    print(S.Fibonacci(39))
