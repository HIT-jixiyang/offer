
def gcd(num):
    gcdl = []
    for i in range(1, sorted(num)[0] + 1):
        for index, j in enumerate(num):
            if j % i == 0:
                if (index + 1) == len(num):
                    gcdl.append(i)
                    break
                continue
            else:
                break
    if not gcdl:
        return 1
    else:
        return sorted(gcdl)[-1]
n=int(input())
A=list(map(int,input().split(' ')))
# print(A)
d=[]
for i in range(1,len(A)):
    d.append(A[i]-A[i-1])
# for i in range(m,-1,-1):
#     flag=0
#     for j in range(len(d)):
#         if d[j]%i!=0:
#             flag=1
#             break
#     if flag==0:
#         print(i)
#         break
k=gcd(d)
if k==1:
    print(-1)
else:
    print(gcd(d))