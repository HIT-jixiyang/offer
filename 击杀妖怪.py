[n,m]=list(map(int,input().split(' ')))
c=[]
w=[]
import math
for i in range(n):
    s=list(map(int,input().split(' ')))
    c.append(s[0])
    w.append(s[1])
G=0
S=0
for i in range(n):
    if w[i]>=math.ceil(c[i]/m):
        if S-c[i]>=0:
            cost=0
            S-=c[i]
        else:
            cost=math.floor((S-c[i]))/m
            if c[i]-S%2==0:
                S=0
            else:
                S=1
        G=G+cost+w[i]
print(math.floor(G))
