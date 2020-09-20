
class Solution:
    def Power(self, base, exponent):
        if exponent==0:
            return 1
        # write code here
        flag = 0
        if exponent < 0:
            flag = 1
            exponent = -exponent
        if flag > 0:
            return 1 / self.fastpower(base,exponent)
        else:
            return self.fastpower(base,exponent)

    def fastpower(self,base,exp):
        if exp==1:
            return base
        else:
            if exp%2==1:
                return self.fastpower(base,exp-1)*base
            else:
                return self.fastpower(base*base,exp>>1)
[m,n]=list(map(int,input().split(' ')))
S=Solution()
print((S.fastpower(m,n)-m*S.fastpower(m-1,n-1))%100003)