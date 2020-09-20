def compare(str1,str2):
    if str1=='':
        return True
    elif str2=='':
        return False
    else:
        len1=len(str1)
        len2=len(str2)
        if len1<len2:
            str1+='#'*(len2-len1)
        else:
            str2+='#'*(len1-len2)
        # print(str1,str2)
        for i in range(len(str1)):
            if str1[i]!='#' and str2[i]!='#':
                if ord(str1[i]) > ord(str2[i]):
                    return True
                elif ord(str1[i]) < ord(str2[i]):
                    return False
                else:
                    continue
            else:
                if str1[i]=='#' and str2[i]!='#':
                    return True
                elif str2[i]=='#' and str1[i]!='#':
                    return False
        return False



L=input().split(',')

# print(compare('z','zc'))
for i in range(len(L)):
    for j in range(0,len(L)-1):
        if not compare(L[j],L[j+1]):
            L[j],L[j+1]=L[j+1],L[j]
print(','.join(L))
