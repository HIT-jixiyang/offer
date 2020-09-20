class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
# write code here
        n=len(matrix)
        m=len(matrix[0])
        ni=min(n,m)
        l=[]
        if ni==1:
            for i in range(n):
                for j in range(m):
                    l.append(matrix[i][j])
            return l
        if ni%2==1:
            p=ni//2+1
        else:
            p=ni//2
        for i in range(p):
            #上 左到右
            # print(matrix[i][i])
            for a in range(i,m-i):
                if matrix[i][a]!='#':
                    # print(matrix[i][a])
                    l.append(matrix[i][a])
                matrix[i][a]='#'
            # print(matrix[i][a+1])
            for b in range(i,n-i):
                if matrix[b][-i-1]!='#':
                    # print(matrix[b][-i-1])
                    l.append(matrix[b][-i-1])
                matrix[b][-i-1]='#'
            # print(matrix[b+1][-i-1])
            for c in range(m-i-1,i-1,-1):
                if matrix[-i-1][c]!='#':
                    # print(matrix[-i-1][c])
                    l.append(matrix[-i-1][c])
                matrix[-i-1][c]='#'
            # print(matrix[-i-1][c-1])

            for d in range(n-i-1,i-1,-1):
                if matrix[d][i]!='#':
                    # print(matrix[d][i])
                    l.append(matrix[d][i])
                matrix[d][i]='#'
        return l