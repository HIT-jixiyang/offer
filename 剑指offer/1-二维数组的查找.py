# -*- coding:utf-8 -*-
#四分发，将正方形区域分成四块求解
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
class Solution:
    # array 二维列表
    def Find(self, target, array):
        n=len(array)-1
        m=len(array[0])-1
        if n==0 or m==0:
            return False
        return self.bin(0,0,n,m,target,array)
    def bin(self,x1,y1,x2,y2,target,array):
        if target<array[x1][y1] or target>array[x2][y2]:
            return False
        if target==array[x1][y1] or target==array[x2][y2]:
            return True
        if x1==x2 and y1==y2:
            return False
        m_x=(x1+x2)//2
        m_y=(y1+y2)//2
        if x1==m_x and y1==m_y:
            return False
        if x2==m_x and y2==m_y:
            return False
        # if array[m_x][m_y]>
        if self.bin(x1, y1, m_x, m_y, target, array):
            return True
        if self.bin(m_x, y1, x2, m_y, target, array):
            return True
        if self.bin(m_x, m_y, x2, y2, target, array):
            return True
        if self.bin(x1, m_y, m_x, y2, target, array):
            return True
        return False



        # write code here
        # m = len(array)
        # n = len(array[0])
        # min1 = 0
        # max1 = m
        # if targer > array[m - 1][n - 1] or target < array[0][0]:
        #     return False
        #
        # while True:
        #     mid = (min1 + max1) // 2
        #     if array[mid][0] == target or:
        #         while True:
        #             min2 = 0
        #             max2 = n
        #             mid2 = (min2 + max2) // 2
        #             if target
        #
        #     if target > array[min1][0] and target < array[max1][0]

