# 2 3
# 1 4 9
# 3 5 9
[m,n]=list(map(int,input().strip().split(' ')))

if m==0 or n==0:
    print(0)
else:
    M = []
    for i in range(m):
        M.append(list(map(int, input().strip().split(' '))))
    dp = [[0] * n for i in range(m)]
    dp[0][0] = M[0][0]
    for i in range(m):
        dp[i][0]=M[i][0]+dp[i-1][0]
    for i in range(n):
        dp[0][i] = M[0][i] + dp[0][i-1]

    for i in range(1,m):
        for j in range(1,n):
            if i==0 and j==0:
                continue
            elif i==0:
                dp[i][j]=dp[i][j-1]+M[i][j]
            elif j==0:
                dp[i][j] = dp[i-1][j]+M[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j],dp[i][j-1]) + M[i][j]
    print(dp[-1][-1])
