def count( k):
        dp = [0]*(k+1)
        if k == 0:return 1
        elif k == 1 :
            return 0
        else:
            dp[2] = 1
            for i in range(3,k+1):
                dp[i] = (dp[i-1] * 2) % (int)(1e9+7)
        return dp[k] * 3

class Solution:
    def Power(self, base, exponent):
        if exponent==0:
            return 1
        # write code here
        flag = 0
        if exponent < 0:
            flag = 1
            exponent = -exponent
        # ans = 1
        # while exponent > 0:
        #     if exponent & 1 == 1:
        #         ans = ans * base
        #     exponent = exponent >> 1
        #     base *= base
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
MOD = 1e9+7
k=int(input().strip())
# if k==0:
#     print(1)
# elif k==1:
#     print(0)
# else:
#     S=Solution()
#     r=S.Power(2,(k-2))
print(int((count(k))%MOD))
# print((2**k)*3%MOD)
# dp=[[0]*4 for i in range(k+1)]
# dp[1][1] = dp[1][2] = dp[1][3] = 1
# for i in range(2,k):
#     for j in range(1,4):
#         for p in range(1,4):
#             if p==j:
#                 continue
#             dp[i][j] = (dp[i][j] + dp[i - 1][p]) % MOD
# dp[k][0] = ((dp[k-1][1] + dp[k-1][2]) % MOD + dp[k-1][3]) % MOD
# print(int(dp[k][0]))