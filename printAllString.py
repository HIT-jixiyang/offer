# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.result=[]
    def Permutation(self, ss):
        # write code here
        if len(ss)==0:
            return []
        chars=[]
        for i in range(len(ss)):
            chars.append(ss[i])
        self.helper(chars,0)
    def helper(self,chars,i):
        if i ==len(chars)-1:
            self.result.append(''.join(chars))
            print(''.join(chars))
        else:
            for j in range(i,len(chars)):
                chars[i],chars[j]=chars[j],chars[i]
                self.helper(chars,i+1)
                chars[i], chars[j] = chars[j], chars[i]




if __name__ == '__main__':
    #abc
    print(ord('a'),chr(91))
    S=Solution()
    S.Permutation('abc')
