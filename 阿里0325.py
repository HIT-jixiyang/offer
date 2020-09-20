
n=int(input())
arr=[]
for i in range(3):
    l=input().split(' ')
    for j in range(len(l)):
        l[j]=int(l[j])
    arr.append(l)
print(arr)
d=[[0]*3 for i in range(n)]
d[0][0]=0
d[0][1]=0
d[0][2]=0

for j in range(1,n):
    d[j][0]=min(d[j-1][0]+abs(arr[0][j-1]-arr[0][j]),d[j-1][1]+abs(arr[1][j-1]-arr[0][j]),d[j-1][2]+abs(arr[2][j-1]-arr[0][j]))
    d[j][1]=min(d[j-1][1]+abs(arr[0][j-1]-arr[1][j]),d[j-1][1]+abs(arr[1][j-1]-arr[1][j]),d[j-1][2]+abs(arr[2][j-1]-arr[1][j]))
    d[j][2]=min(d[j-1][2]+abs(arr[0][j-1]-arr[2][j]),d[j-1][1]+abs(arr[1][j-1]-arr[2][j]),d[j-1][2]+abs(arr[2][j-1]-arr[2][j]))

print(min(d[-1][0],d[-1][1],d[-1][2]))



