# print(6&2)

n=int(input())
A=list(map(int,input().split(' ')))
def getSim(A,a,flag):
    ans=[]
    exsit=0
    for i in range(len(A)):
        if  A[i]!=a and A[i]&a==0 :
            if flag[i]==1:
                exsit=1
            else:
                ans.append(i)
    if len(ans)>0:
        return ans
    elif exsit:return [-1]
    else:
        return ans
ans=[-1]*n
count=0
for i in range(len(A)):
    if ans[i]==1:
        continue
    j=getSim(A, A[i],ans)
    if j:
        if j[0]==-1:
            ans[i]=1
            count+=1
            continue
        else:
            ans[i] = 1
            for p in j:
                ans[p] = 1
            count += len(j)
        if count >= n:
            break
ans=map(str,ans)
print(' '.join(ans))





