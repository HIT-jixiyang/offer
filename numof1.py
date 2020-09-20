# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count=0
        for i in range(n+1):

            while True:
                t=i%10
                if t==1:
                    count+=1
                i=i//10
                if i==0:
                    break
        return count


if __name__ == '__main__':
    S=Solution()
    print(S.NumberOf1Between1AndN_Solution(5))