#位运算，与进位，异或本位
# 执行加法 x ^ y
# 进位操作 ( x & y ) << 1
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        if num2 + num1 == 1 :return 1
        su = num1^num2
        carry = (num1 & num2)<<1
        num1,num2 = su,carry
        while str(num2) != '0' :
            num1,num2 = num1^num2,(num1 & num2)<<1
        return num1