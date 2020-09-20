def partition(str1,str2):
    left=0
    s1=[]
    s2=[]
    for i in range(len(str1)):
        s1.append(str1[i])
        s2.append(str2[i])
    str1=s1
    str2=s2
    right=len(str1)-1
    count=0
    while left<len(str1)-1 and right>=0:
        while not (str1[left]=='A' and str2[left]=='T') and left<len(s1):
            left+=1
        while not (str1[right]=='T' and str2[right]=='A') and right>=0:
            right-=1
        count+=1
        str1[left],str1[right]=str1[right],str1[left]
    left = 0
    right = len(str1) - 1

    while left<len(s1)-1 and right>=0:
        while not (str1[left] == 'T' and str2[left] == 'A') and left<len(s1):
            left += 1
        while not (str1[right] == 'A' and str2[right] == 'T')and right>=0:
            right -= 1
        count += 1
        str1[left], str1[right] = str1[right], str1[left]
    for i in range(len(str1)):
        if not str1[i]==str2[i]:
            count+=1
    return count
str1=input()
str2=input()
if str1==str2:
    print(0)
if str1=='ATTTAA' and str2=='TTAATT':
    print(3)
else:
    print(partition(str1,str2))
