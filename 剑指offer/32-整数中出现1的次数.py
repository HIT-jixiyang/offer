#下面是不考虑时间复杂度的解法
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count=0
        for i in range(n+1):

            while True:
                t=i%10
                if t==1:
                    count+=1
                i=i//10
                if i==0:
                    break
        return count
#比较节约时间的方法是
# 以  n =216为例：
# 个位上： 1 ，11，21，31，.....211。个位上共出现（216/10）+ 1个 1 。
# 因为除法取整，210~216间个位上的1取不到，所以我们加8进位。你可能说为什么不加9，
# n=211怎么办，这里把最后取到的个位数为1的单独考虑，先往下看。
# 十位上：10~19，110~119，210~216.
# 十位上可看成 求（216/10）=21 个位上的1的个数然后乘10。
# 这里再次把最后取到的十位数为1的单独拿出来，即210~216要单独考虑 ，
# 个数为（216%10）+1 .这里加8就避免了判断的过程。


# public int NumberOf1Between1AndN_Solution(int n) {
#     int cnt = 0;
#     for (int m = 1; m <= n; m *= 10) {
#         int a = n / m, b = n % m;
#         cnt += (a + 8) / 10 * m + (a % 10 == 1 ? b + 1 : 0);
#     }
#     return cnt;
# }