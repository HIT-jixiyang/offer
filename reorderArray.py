# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        left=0
        right=len(array)-1
        odd=[]
        even=[]
        for i in range(len(array)):
            if array[i]%2==1:
               odd.append(array[i])
            if array[i]%2==0:
                even.append(array[i])
        array=odd+even
        # while left<right:
        #     while array[left]%2==1:
        #         left+=1
        #     while array[right]%2==0:
        #         right-=1
        #     array[left],array[right]=array[right],array[left]
        return array
if __name__ == '__main__':
    S=Solution()
    print(S.reOrderArray([1,2,3,4,5,6,7,8,9]))
