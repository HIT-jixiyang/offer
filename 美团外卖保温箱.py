def sec(elem):
    return elem[1]

n=int(input())
C=list(map(int,input().split(' ')))
A=list(map(int,input().split(' ')))
P=[]
for i in range(len(C)):
    P.append([C[i],A[i]])
P.sort(key=sec)
all=sum(C)

# print(P)
s=0
y=0
num=0
for i in range(len(P)-1,-1,-1):
    if P[i][1]>
    if i-1>=0 and P[i][1]>P[i-1][1] and all<=P[i-1][1]:
        continue
    s=s+P[i][1]
    y+=P[i][0]
    num+=1
    if s>=all:
        break
box_num=num
seconds=all-y
print(box_num,seconds)


