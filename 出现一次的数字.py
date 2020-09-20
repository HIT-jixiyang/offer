# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return []
        result=array[0]
        for i in range(1,len(array)):
            result=result^array[i]
        index=1
        while index & result==0:
            index=index<<1
        result1=0
        result2=0
        for i in range(len(array)):
            if index&array[i]==0:
                result1=result1^array[i]
            else:
                result2=result2^array[i]
        return [result1,result2]

        #a^b

if __name__ == '__main__':
    S=Solution()
    print(S.FindNumsAppearOnce([1,1,2,2,3,3,4,4,5,6]))
