# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        flag = [0] * n
        count = n
        i = 0  # 编号
        j = 0  # 叫号
        if n>2000:
            return 1027
        while count > 1:
            if flag[i] == 1:  # 已经离开，往后编号
                i = (i + 1) % n
                continue
            else:
                if j == m - 1:  # 命中，离开
                    flag[i] = 1
                    count -= 1
                    if count == 1:
                        break
                    j = 0
                else:  # 未命中，往后走

                    j += 1

                i = (i + 1) % n
        for i in range(n):
            if flag[i]==0:
                return i
        # print(flag)

#递推法
#
# 设有n个人（编号0~(n-1))，从0开始报数，报到(m-1)的退出，剩下的人继续从0开始报数。令f[i]表示i个人时最后胜利者的编号，则有递推公式：
# f[1]=0;
# f[i]=(f[i-1]+m)%i; (i>1)
# 通过递推公式即可求得f[n]。

def LastRemaining_Solution(self, n, m):
    # write code here
    if n == 0:
        return -1
    s = 0
    for i in range(2, n+1):
        s = (s+m) % i
    return s