# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers)==0:
            return 0
        for i in range(len(numbers)):
            numbers[i]=str(numbers[i])
        for i in range(len(numbers)):

            for j in range(0,len(numbers)-1-i):
                if not self.compare(numbers[j],numbers[j+1]):

                    numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
        return int(('').join(numbers))
    def compare(self,s1,s2):
        if int(s1+s2)<int(s2+s1):
            return True
        else:
            return False
if __name__ == '__main__':
    S=Solution()
    print(S.PrintMinNumber([3,32,321]))