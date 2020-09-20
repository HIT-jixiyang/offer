class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n==1:
            return 1
        i=1
        t=1
        a=0
        b=0
        c=0
        t=[1]*n
        while i<n:
            s=min([t[a]*2,t[b]*3,t[c]*5])
            if s==t[a]*2:
                a+=1
            if s==t[b]*3:
                b+=1
            if s==t[c]*5:
                c+=1
            t[i]=s
            i+=1
        return s
S=Solution()
print(S.nthUglyNumber(10))