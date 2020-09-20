class Solution:
    def fourSum(self,nums,target):

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []

        for i in range(n-3):
            if (i>0) and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if (j>i+1 and nums[j]==nums[j-1]):
                    continue
                L = j + 1
                R = n - 1
                while (L < R):
                    if (nums[i] + nums[L] + nums[R]+nums[j] == target):
                        res.append([nums[i], nums[j],nums[L], nums[R]])
                        while (L < R and nums[L] == nums[L + 1]):
                            L = L + 1
                        while (L < R and nums[R] == nums[R - 1]):
                            R = R - 1
                        L = L + 1
                        R = R - 1
                    elif (nums[i] + nums[L] + nums[R]+nums[j] > target):
                        R = R - 1
                    else:
                        L = L + 1
        return res
if __name__ == '__main__':
    S=Solution()
    print(S.fourSum([-3,-2,-1,0,0,1,2,3],0))

