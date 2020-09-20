def ugly_str(s):
    array=[]
    for c in s :
        array.append(c)
    s=array
    d_a = [0] * (len(s)+1)
    d_b = [0] * (len(s)+1)
    for i in range(2, len(s) + 1):
        if s[i - 1] == s[i - 2] and s[i-1]!='?':
            d_a[i] = d_a[i - 1] + 1
            d_b[i] = d_b[i - 1] + 1
        else:
            if s[i - 1] == '?':
                if i-1==0:
                    s[i-1]='A'
                    continue
                d_a[i] = d_a[i - 1]
                d_b[i] = d_b[i - 1]
                if s[i-2]=='A':
                    s[i-1]='B'
                elif s[i-2]=='B':
                    s[i-1]='A'
            else:
                d_a[i] = d_a[i - 1]
                d_b[i] = d_b[i - 1]
    return min(d_a[-1], d_b[-1])
s=input()
print(ugly_str(s))
