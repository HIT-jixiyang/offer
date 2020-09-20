def perfect(a,b):
    t=a[0]+b[0]
    for i in range(1,len(a)):
        if a[i]+b[i]!=t:
            return False
    return True


[n,k]=list(map(int,input().split(' ')))
A=[]
S=[]
flag=[0]*n
for i in range(n):
    A.append(list(map(int,input().split(' '))))
    S.append(sum(A[i]))
c=0
for i in range(n):
    if flag[i]==1:
        continue
    for j in range(n):
        if i==j:
            continue

        else:
            if perfect(A[i],A[j]) :
                c+=1
                flag[i]=1
                flag[j]=1
print(c//2)

