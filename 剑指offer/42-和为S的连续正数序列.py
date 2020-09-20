class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        result=[]
        if tsum==1 or tsum==2:
            return []
        else:
            for n in range(tsum,1,-1):
                if (2*tsum-n*n+n) % (2*n)==0 and 2*tsum-n*n+n>0:
                    start=(2*tsum-n*n+n) //(2*n)
                    if start==0:
                        continue
                    result.append(range(start,start+n))
        return result