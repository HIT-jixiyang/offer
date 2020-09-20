def max_pre(str1,str2):

    for i in range(min(len(str1),len(str2))):
        if str1[i]!=str2[i]:
            return i
    if len(str1)<len(str2):
        return len(str1)
    else:
        return len(str2)

n=int(input())
L=[]
for i in range(n):
    L.append(input())
i=1
while i<=100:
    i+=1
    try:
        p=input().split(' ')
    except:
        break
    p[0]=int(p[0])-1
    p[1]=int(p[1])-1
    print(max_pre(L[p[0]],L[p[1]]))
