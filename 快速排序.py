def quicksort1(arr,left,right):
    if left<right:

        m=partition(arr,left,right)
        quicksort1(arr,left,m-1)
        quicksort1(arr,m+1,right)
    else:
        return
def quicksort2(arr,left,right):
    stack=[]
    stack.append([left,right])
    while len(stack)>0 and left<right:
        left,right=stack.pop(-1)
        m=partition(arr,left,right)
        if left<m-1:
            stack.append([left,m-1])
        if m+1<right:
            stack.append([m+1,right])



def partition(arr,left,right):
    pivot=arr[left]
    while left<right:
        while arr[right]>=pivot and left<right:
            right-=1
        arr[left]=arr[right]
        while arr[left]<=pivot and left<right:
            left+=1
        arr[right]=arr[left]
    arr[left]=pivot
    return left



if __name__ == '__main__':
    A=[6,5,4,3,2,1]
    quicksort2(A,0,len(A)-1)
    print(A)
