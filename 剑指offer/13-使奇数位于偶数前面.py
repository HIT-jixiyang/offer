# -*- coding:utf-8 -*-
# class Solution:
#     def reOrderArray(self, array):
#         # write code here
#         left=0
#         right=len(array)-1
#         odd=[]
#         even=[]
#         for i in range(len(array)):
#             if array[i]%2==1:
#                 odd.append(array[i])
#             if array[i]%2==0:
#                 even.append(array[i])
#         array=odd+even
#         return array
class Solution:
    def reOrderArray(self, array):
        for i in range(1,len(array)):
            for j in range(1,len(array)):
                if array[j-1]%2==0 and array[j]%2==1:
                    array[j - 1],array[j]=array[j],array[j-1]
        print(array)
if __name__ == '__main__':
    S=Solution()
    S.reOrderArray([1,2,3,4,5])