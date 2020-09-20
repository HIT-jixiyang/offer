
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n==0:
            return 0
        count=0
        if n<0:
            count=1
            i=0
            while i<31:
                t = n & 1
                if t == 1:
                    count += 1
                n = n >> 1
                i+=1
        else:
        #     count+=1
            while n>0:
                t=n&1
                if t==1:
                    count+=1
                n=n>>1
        return count
if __name__ == '__main__':
    S=Solution()
    print(S.NumberOf1(-1))
