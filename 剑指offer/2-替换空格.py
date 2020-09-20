
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        t=''
        for c in s:
            if c==' ':
                t=t+'%20'
            else:
                t=t+c
            # print(c)
        return t