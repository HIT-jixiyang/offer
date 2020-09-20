def getGold(list,n):
    d=[[0]*(n+1) for i in range(n+1)]
    l=[0]*(n+1)
    l[1:]=list
    list=l
    for i in range(1,n+1):
        d[i][i] = list[i]
        if i+1<=n:
            d[i][i+1]=max(list[i],list[i+1])
    for i in range(n,0,-1):
        for j in range(i+1,n+1):
            d[i][j] =max(sum(list[i:j+1])-d[i+1][j],sum(list[i:j+1])-d[i][j-1])
    return d[1][n],sum(list)-d[1][n]
samples_n=int(input())
for i in range(samples_n):
    n=int(input())
    l=input().split(' ')
    for j in range(len(l)):
        l[j]=int(l[j])
    r=getGold(l,n)
    print('Case #'+str(i+1)+':'+str(r[0])+str(r[1]))
