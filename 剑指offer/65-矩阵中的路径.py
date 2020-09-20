# -*- coding:utf-8 -*-
import copy
class Solution:
    matrix=''
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        #'abcdef'

        m=[]
        start=[]
        for i in range(rows):
            n=[]
            for j in range(cols):
                n.append(matrix[i*cols+j])
            m.append(n)
        self.matrix=m
        for i in range(rows):
            for j in range(cols):
                if self.matrix[i][j] == path[0]:
                    start.append((i, j))
        for s in start:

            if self.find(s[0],s[1],path[1:],self.matrix):
                return True
        return False

    def find(self,x,y,path,m):

        matrix=copy.deepcopy(m)
        matrix[x][y] = '#'
        if x>=len(matrix) or y>=len(matrix[0]):
            return False
        if len(path) == 0:
            return True
        if x>0:
            if matrix[x-1][y]==path[0]:
                matrix[x - 1][y]='#'
                if self.find(x-1,y,path[1:],matrix):
                    return True
        if y>0:
            if matrix[x][y-1]==path[0]:
                matrix[x][y-1]='#'
                if self.find(x,y-1,path[1:],matrix):
                    return True
        if x+1<len(matrix):
            if matrix[x+1][y]==path[0]:
                matrix[x + 1][y]='#'
                if self.find(x+1,y,path[1:],matrix):
                    return True
        if y+1<len(matrix[0]):
            if matrix[x][y+1]==path[0]:
                matrix[x][y + 1]='#'
                if self.find(x,y+1,path[1:],matrix):
                    return True
        return False