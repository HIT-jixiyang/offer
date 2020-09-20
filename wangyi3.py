import itertools
[n,k]=input().split(' ')
n=int(n)
k=int(k)
A=[]

for i in range(k):
    A.append(''.join(input().split(' ')))
P=list(itertools.permutations(range(1,n+1)))
if k==0:
    for i in range(len(P)):
        # P[i]=' '.join(P[i])
        for j in range(n):
            if j==n-1:
                print(P[i][j])
            else:
                print(P[i][j],end=' ')
else:
    for i in range(len(P)):
        # P[i]=' '.join(P[i])
        P[i]=''
        for j in range(n):
            P[i]+=P[j]
        flag=0
        for k in range(len(A)):
            if P[i].__contains__(A[i]):
                flag=
                break





