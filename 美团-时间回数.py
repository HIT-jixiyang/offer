def getdate(H,M):
    if H<10:
        str1='0'+str(H)
    else:
        str1=str(H)
    if M<10:
        str2='0'+str(M)
    else:
        str2 = str(M)
    return str1+':'+str2
n=int(input())
s=input()
m=int(input())
[now_h,now_m]=s.split(':')
now_h=int(now_h)
now_m=int(now_m)
if m<now_m:
    print(n)
    print(getdate(now_h,now_m-m))
elif m<=now_h*60+now_m:
    print(n)
    d=now_h*60+now_m-m
    print(getdate(d//60,d%60))
else:
    m=m-now_h*60-now_m
    days=m//(60*24)+1
    left=m%(60*24)
    h=(24*60-left)//60
    m=(24*60-left)%60
    t=getdate(h,m)
    d=(n-days)%7
    if d==0:
        print(7)
    else:
        print(d)
    print(t)
