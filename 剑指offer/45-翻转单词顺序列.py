# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if  not s:
            return s
        s1=s.split()
        if len(s1)==0:
            return s
        else:
            s2=[]
            for i in s1:
                s2.append(i)
                s2.append(' ')
            s2.reverse()
            return ''.join(s2).strip()
        #strip默认去掉字符串开头或者结尾的空格或者换行符