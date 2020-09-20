import math
def sift(li, low, higt):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= higt:  # 情况2：i已经是最后一层
        if j + 1 <= higt and li[j + 1] >= li[j]:  # 右孩子存在并且小于左孩子
            j += 1
        if tmp <= li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break  # 情况1：j位置比tmp小
    li[i] = tmp
def build_heap(li):
    heap = li[:]
    # 建堆
    k=len(heap)
    for i in range(k // 2 - 1, -1, -1):
        sift(heap, i, k - 1)
    return heap
def top_k(li, k):
    heap = li[:]
    # 建堆
    for i in range(k, len(li)):
        if li[i] < heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    # 挨个输出
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap

s=input()
s=s.split(' ')
n=int(s[0])
m=int(s[1])

init=list(map(int,input().split(' ')))
init=build_heap(init)
print(init)

Q=int(input())

questions=[]
for i in range(Q):
    questions.append(int(input()))
max_q=0
for i in range(Q):
    if questions[i] % m==0:
        days=questions[i]//m
    else:
        days=questions[i]//m+1
    if questions[i]>max_q:
        init=top_k(init,questions[i])
        max_q=questions[i]
    # print(init)
    ready=init[:questions[i]]
    ready.reverse()
    ans=0
    for j in range(days):
        if j*m+m>questions[i]:
            end=questions[i]
        else:
            end=j*m+m
        ans+=(j+1)*sum(ready[j*m:end])
    print(ans)

