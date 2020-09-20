# -*- coding:utf-8 -*-
#获得大小王索引
def getJK_index(numbers):
    J = []
    for i in range(len(numbers)):
        if numbers[i] == 0:
            J.append(i)
    return J


def getmin(numbers):
    min_ = 100
    for i in range(len(numbers)):
        if numbers[i] <= min_ and numbers[i] != 0:
            min_ = numbers[i]
    return min_


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) == 0:
            return False
        min_p = getmin(numbers)
        max_p = max(numbers)

        J = getJK_index(numbers)
        num_j = len(J)
        flag = 0
        count = 0
        d = {}
        for i in range(1, len(numbers)):
            if numbers[i] in numbers[:i] and numbers[i] != 0:
                return False
        for i in range(min_p, max_p):
            if not i in numbers:
                count += 1

        if count <= num_j:
            return True
        else:
            return False