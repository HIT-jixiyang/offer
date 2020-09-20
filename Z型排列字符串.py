nk=input()
nk=nk.split()
n,k=int(nk[0]),int(nk[1])
confict={}
for line in range(k):
    line=input()
    tempstr=line.split()
    stu1,stu2=int(tempstr[0]),int(tempstr[1])
    confict[stu1]=confict.get(stu1,set())
    confict[stu1].add(stu2)
    confict[stu2]=confict.get(stu2,set())
    confict[stu2].add(stu1)
stus=[i+1 for i in range(n)]
res=[]
def permutation(path,rest):
    if not rest:return res.append(path)
    for i in range(len(rest)):
        if path and rest[i] in confict.get(path[-1],set()):continue
        permutation(path+[rest[i]],rest[:i]+rest[i+1:])
permutation([],stus)
# print(confict)
for i in range(len(res)):
    temp=map(lambda x:str(x),res[i])
    print(" ".join(temp))