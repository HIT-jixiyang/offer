n=int(input().strip())
A=input().strip().split(' ')
for i in range(len(A)):
    # print(A[i])
    A[i]=int(A[i])
B=input().strip().split(' ')

for i in range(len(B)):
    B[i]=int(B[i])
d={}
result=0

for i in range(n):
    d[B[i]]=i+1
maxpos=0
for i in range(n):
    curpos=d[A[i]]
    if curpos<maxpos:
        result+=1
    maxpos=max(curpos,maxpos)
print(result)

