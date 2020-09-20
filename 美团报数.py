def get_first(flag_A):
    for i in range(len(flag_A)):
        if flag_A[i]==0:
            return i
class Solution:
    def LastRemaining_Solution(self, n, A):
        # write code here
        ans=[]
        if n == 0:
            return -1
        flag = [0] * n
        count = 0
        i = 0  # 编号
        j = 0  # 叫号
        while count <n:
            if flag[i] == 1:  # 已经离开，往后编号
                i = (i + 1) % n
                continue
            else:
                if j == A[count]:  # 命中，离开
                    flag[i] = 1
                    ans.append([i+1,n-count])
                    count += 1
                    if count == n:
                        break
                    j = 0
                    i=get_first(flag)

                else:  # 未命中，往后走

                    j += 1

                i = (i + 1) % n
        return ans
n=int(input())
A=list(map(int,input().split(' ')))
S=Solution()
ans=S.LastRemaining_Solution(n,A)
print(ans)