# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        l=[0]*(number+100)
        l[1]=1
        l[2]=2
        l[3]=3
        if number<=3:
            return l[number]

        for i in range(3,number+1):
            l[i]=l[i-1]+l[i-2]
        return l[number]

