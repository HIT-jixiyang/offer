[n,k]=list(map(int,input().split(' ')))
item=[]
price=[]
type=[]
for i in range(n):
    [u,v]=(list(map(int,input().split(' '))))
    price.append(u)
    type.append(v)
if n==1 or k==1 :
    if min(type)==2:
        print(sum(price))
    else:
        print(sum(price)/2)
elif sum(type)==n+1:
    price.sort()
    print(sum(price)-price[1]/2)
elif sum(type) == n + 2:
    price.sort()
    print(sum(price) - price[0] / 2-price[-1]/2)
else:
    price.sort()


