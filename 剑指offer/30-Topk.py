# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k>len(tinput) or k<=0 or not tinput:
            return []
        left=0
        right=len(tinput)-1
        pivot=self.partition(tinput,left,right)
        while pivot!=k-1:
            if pivot<k-1:
                left=pivot+1
                pivot=self.partition(tinput,left,right)
            else:
                right=pivot-1
                pivot= self.partition(tinput,left,right)
        return sorted(tinput[:k])
# write code here
    def partition(self,arr,left,right):
        pivot=arr[left]
        while left<right:
            while left<right and arr[right]>=pivot:right-=1
            arr[left]=arr[right]
            while left<right and arr[left]<=pivot:left+=1
            arr[right]=arr[left]
        arr[left]=pivot
        return left