n=int(input())

l=[0]
h=[0]
for i in range(n):
    s=input().split(' ')
    l.append(int(s[0]))
    h.append(int(s[1]))
d=[0]*(n+1)
d[1]=max(l[1],h[1])
for i in range(2,n+1):
    d[i]=max(d[i-1]+l[i],d[i-2]+h[i])
print(d[n])