[n,D]=input().split(' ')
n=int(n)
D=int(D)
A=list(map(int,input().split(' ')))
B=list(map(int,input().split(' ')))
hurt=0
master=[]
if max(A)<=D:
    print(0)
if min(A)>D:
    print(sum(B))
else:
    for i in range(n):
        for j in range(i,n-1):
            if A[i]<A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                B[i],B[i+1]=B[i+1],B[i]
    t=0
    for i in range(n):
        if A[i]<=D:
            t=i+1
            continue
        master.append([A[i],B[i]])
    D+=t

for i in range(len(master)):
    if D>=master[i][0]:
        D+=1
    else:
        hurt+=master[i][1]
print(hurt)

