def LCS(s1,s2):
    pass
str_list=[]
def kuohao(f,n):
    global str_list
    if len(f)+2==n:
        str_list.append('()'+f)
        str_list.append('({})'.format(f))
        str_list.append(f+'()')
    else:
        kuohao('()'+f,n)
        kuohao('({})'.format(f),n)
        kuohao(f+'()',n)


def getNum(s):
    c=-1
    for i in range(len(s)):
        if s[i]=='(':
            c=i
    return c

def getNum2(s):
    c=-1
    for i in range(len(s)):
        if s[i]==')':
            c=i
    return c


str1=input()
kuohao('',len(str1))
# print(set(str_list))
str_list=set(str_list)
print(str_list)
# print(getNum(str1))
r1=0
r2=0

for s in str_list:
    if s==str1:
        continue
    # print(getNum(s),getNum(str1))
    if getNum(s)<=getNum(str1):
        r1+=1
for s in str_list:
    if s==str1:
        continue
    # print(getNum2(s),getNum2(str1))
    if getNum(s)>=getNum(str1):
        r2+=1

print(max(r1,r2))
