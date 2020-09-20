# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        for i in range(len(rotateArray)):
            if rotateArray[i]>rotateArray[i+1]:
                t=rotateArray[i+1]
                break
        if i==len(rotateArray)-1:
            t=rotateArray[0]
        return t
if __name__ == '__main__':
    S=Solution()
    print(S.minNumberInRotateArray([3,4,5,2,2,3]))