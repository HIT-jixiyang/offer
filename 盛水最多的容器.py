class Solution:
    def maxArea(self, height):
        max_c = 0
        l = len(height)
        max_height=0
        max_height2=0
        for i in range(l):
            if height[i]<max_height:
                # max_height=height[i]
                # print('continue')
                continue
            else:
                max_height = height[i]
            for j in range(l-1, i,-1):
                if max_height2>height[j] :
                    
                    # print('continue')
                    continue
                else:

                    t = min(height[i], height[j]) * (j - i)
                    if max_c < t:
                        max_height2 = height[j]
                        max_c = t
        return max_c

if __name__ == '__main__':
    h=[1,8,6,2,5,4,8,3,7]
    S=Solution()
    print(S.maxArea(h))