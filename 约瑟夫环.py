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
if __name__ == '__main__':
    S=Solution()
    print(S.LastRemaining_Solution(4000,997))