


n=int(input())
m=int(input())


A=input().split(' ')
B=input().split(' ')
T=[[0,0]]
for i in range(len(A)):
    A[i]=int(A[i])

    B[i]=int(B[i])
    T.append([A[i],B[i]])
sorted(T,key=lambda  x:x[1],reverse=True)
dp=[[0]*200 for i in range(200)]
print(T)
#
# flag=0
# while
# for i in range(n):
#
for i in range(1,n+1):
    max_j = min(i, m)
    for j in range(1,max_j):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + T[i][0] - T[i][1] * (j - 1));
print(dp[n][m])
# 	for (int i = 1; i <= n; i++)//进行dp
# 	{
# 		int maxj = min(i, m);//f[i][j]表示的是前i个数擦掉j个数的最大值
# 		for (int j = 1; j <= maxj; j++) //j则不能超过i.但要到达m；
# 			f[i][j] = max(f[i - 1][j], f[i - 1][j - 1] + a[i] - b[i] * (j - 1));
# 	}
# 	printf("%d\n", f[n][m]);//输出答案。
# 	return 0;
# }
#
#
