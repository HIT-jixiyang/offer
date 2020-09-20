class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        flag = 0
        if (divisor < 0 and dividend > 0):
            divisor = -divisor
            flag = 1
        elif (divisor > 0 and dividend < 0):
            dividend = -dividend
            flag = 1
        elif (divisor < 0 and dividend < 0):
            dividend = -dividend
            divisor = -divisor
        tmp1 = divisor
        tmp2 = tmp1 + tmp1
        if dividend < divisor:
            return 0
        if dividend < divisor + divisor:
            if flag>0:
                return -1
            else:
                return 1
        result = 0
        while dividend>=divisor:
            origin=dividend
            tmp1 = divisor
            tmp2 = tmp1 + tmp1
            if dividend<divisor+divisor:
                result+=1
                break
            r=1
            while True:
                if dividend >= tmp2:
                    tmp1 = tmp2
                    tmp2 = tmp1 + tmp1
                    r += r
                    dividend = origin- tmp1
                else:
                    break


            result+=r


        if result>2**31-1 and flag==0:
            result=2**31-1
            return result
        if result>2**31-1 and flag==1:
            result=-2**31
            return result
        if flag==1:
            return -result
        else:
            return result
if __name__ == '__main__':
    S=Solution()
    print(S.divide(-2147483648,1))
    # print(2**32)