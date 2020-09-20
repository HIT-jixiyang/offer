
n=int(raw_input())
l=raw_input().split(' ')
for i in range(len(l)):
    l[i]=int(l[i])
count=[0]*9
seqs=[]
start=0
for i in range(len(l)):
    if count[l[i]]==1:
        seqs.append(l[start:i])
        count=[0]*9
        start=i
    else:
        count[l[i]]+=1
if start<len(l):
    seqs.append(l[start:])
c=1
for i in range(len(seqs)):
    c*=2**(len(seqs[i])-1)
print c
