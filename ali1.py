import math
import heapq
def ji(n , m, k, arr):
    for i in range(m):
        arr = [x+k for x in arr]
        maxidx = arr.index(max(arr))
        arr[maxidx] = math.floor(arr[maxidx]/2)
        # print(arr)
    return sum(arr)
def get_max(arr):
    ma=arr[0]
    index=0
    for i in range(1,len(arr)):
        if ma<arr[i]:
            ma=arr[i]
            index=i
    return index,ma
s=input()
s=s.split(' ')
n=int(s[0])
m=int(s[1])
k=int(s[2])
init=input().split(' ')

if n==0:
    print(0)
if m==1:
    print(sum(init)-max(init)//2)

for i in range(len(init)):
    init[i]=int(init[i])
print(ji(n,m,k,init))
# for i in range(m):
#     for c in range(n):
#         init[c]+=k
#     max_index,ma=get_max(init)
#     init[max_index]-=(init[max_index]//2)
# print(sum(init))
#
#
