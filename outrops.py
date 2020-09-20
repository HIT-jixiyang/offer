class Solution:
    def cutRope(self, number):
        # write code here
        if number==1:
            return 1
        if number==2:
            return 1
        if number==3:
            return 2
        if number==4:
            return 4
        r=number%3
        n_3=number//3
        n_2=r//2
        n_1=r%2
        t3=3**n_3
        t2=2**n_2
        return t3*t2
class Solution2:
    def cutRope(self, number):
        # write code here
        if number==1:
            return 1
        if number==2:
            return 1
        if number==3:
            return 2
        d={}
        d[1]=1
        d[2]=2
        d[3]=2
        m=0
        for i in range(4,number+1):
            for j in range(1,i//2+1):
                if m<d[j]*d[i-j]:
                    m=d[j]*d[i-j]
            d[i]=m
        return m

if __name__ == '__main__':
    S=Solution()
    print(S.cutRope(5))

