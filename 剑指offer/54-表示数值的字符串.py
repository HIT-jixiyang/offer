# -*- coding:utf-8 -*-

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            s = float(s)
            return True
        except:
            return False
#正规解法应该为：分情况讨论
# +-号后面必定为数字或后面为.（-.123 = -0.123）
# +-号只出现在第一位或在eE的后一位
# .后面必定为数字或为最后一位（233. = 233.0）
# eE后面必定为数字或+-号