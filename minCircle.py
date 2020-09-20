def bubleSort(arr):
    # max_n=arr[0]
    # for i in range(len(arr)):
    #     for j in range(i,len(arr)):
    #         if arr[j-1]<arr[j]:
    #
    #         if arr[i]>max_n:
    #             max_n=arr[0]

    sorted_array=sorted(arr)
    return sorted_array
n=int(input())
height_list=(input()).split(' ')
for i in range(len(height_list)):
    height_list[i]=int(height_list[i])
s_arr=bubleSort(height_list)


mid=n//2
m=s_arr[mid]
s_arr=s_arr[:mid]+s_arr[mid+1:]
min_loss=0
for i in range(1,len(s_arr)):
    if s_arr[i]-s_arr[i-1]>min_loss:
        min_loss=s_arr[i]-s_arr[i-1]
print(max(min_loss,m-s_arr[0],s_arr[-1]-m))
print(s_arr.reverse())



