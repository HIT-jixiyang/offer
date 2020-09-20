class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length=len(nums)
        target=0
        if length%2==1:
            pos=length//2+1
        else:
            pos=length//2
        target=nums[pos-1]
        count=0
        for i in range(pos-1):
            count+=target-nums[i]
        for i in range(pos,length):
            count+=nums[i]-target
        return count


if __name__ == '__main__':
    [n,k]=list(map(int,input().split(' ')))
    A=list(map(int,input().split(' ')))
    # print(vars(A))
    S=Solution()

    A.sort()
    d=(A[-1]-A[0])**2
    start=0
    for i in range(0,n-k):
        c= S.minMoves2(A[i:i+k])
        if c<d:
           d=c
    print(d)