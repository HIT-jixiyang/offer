#递归写法


class Solution:
    def cutRope(self, number):
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        return self.cutRopeCore(number)

    def cutRopeCore(self, number):
        if number < 4:
            return number
        max_ = 0
        for i in range(1, number / 2 + 1):
            max_ = max(self.cutRopeCore(i) * self.cutRopeCore(number - i), max_)
        return max_
#自底向上
链接：https: // www.nowcoder.com / questionTerminal / 57
d85990ba5b440ab888fc72b0751bf8?answerType = 1 & f = discussion
来源：牛客网


class Solution:
    def cutRope(self, number):
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
            # 申请辅助空间
        products = [0] * (number + 1)
        # 定义前几个初始变量的值
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        # 进行动态规划,也就是从下向上的进行求解
        for i in range(4, number + 1):
            max_ = 0
            for j in range(1, i / 2 + 1):
                max_ = max(products[j] * products[i - j], max_)
            products[i] = max_

        max_ = products[number]
        return max_

#贪婪算法，首先尽量剪成长度为3的，然后是长度为2的，不能出现长度为1的

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