[n,k]=list(map(int,input().strip().split(' ')))
def check(x,n,k):
    sum=0
    while x>0:
        sum+=x
        x=x//k
    return sum>=n
# print(n,k)
if k>n:
    print(n)
else:
    l=1
    r=n
    while l<r:
        mid=l + ((r - l) >> 1)
        if check(mid,n,k):
            r=mid
        else:
            l=mid+1
    print(l)