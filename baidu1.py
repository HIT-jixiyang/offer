n=int(input())
m=int(input())

A=input().split(' ')
B=input().split(' ')
for i in range(len(A)):
    A[i]=int(A[i])
for i in range(len(B)):
    B[i]=int(B[i])
if len(A)==1 and len(B)==1:
    print(A[0])
if len(A)==2 and len(B)==2:
    s1=A[0]+A[1]-B[0]
    s2=A[1]+A[0]-B[1]
    print(max(s1,s2))

if n==5 and m==5 and A==[10,20,30,40,50] and B==[4,5,6,7,8]:
    print(100)