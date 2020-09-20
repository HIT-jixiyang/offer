import heapq
s=input()
s=s.split(' ')
n=int(s[0])
m=int(s[1])
k=-int(s[2])
init=input().split(' ')
q=[]
for i in range(len(init)):
    heapq.heappush(q,-int(init[i]))
    # q.append()
sum=0
for i in range(1,m+1):
    sum+=k
    tmp=heapq.heappop(q)
    tmp+=sum
    tmp/=2
    tmp-=sum
    q.append(tmp)
ans=0
while len(q)>0:
    ans+=heapq.heappop(q)+sum

print(-ans)


