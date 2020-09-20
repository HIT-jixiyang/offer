def getSum(l):
    s=0
    for i in range(len(l)):
        for j in range(len(l[0])):
            s+=l[i][j]
    return s


class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)<=1 or len(board[0])<=1:
            return board


        visit=[[0]*len(board[0]) for i in range(len(board))]
        i=0
        j=0
        color=[]
        while getSum(visit)<len(board)*len(board[0]):
            queue = []
            area = []
            fit=True
            for i in range(len(board)):
                find=0
                for j in range(len(board[0])):

                    if board[i][j]=='O' and visit[i][j]==0:
                        queue.append([i,j])
                        visit[i][j]=1
                        find=1
                        break
                    else:
                        visit[i][j] = 1
                if find>0:
                    break
            while len(queue)>0:
                [x,y]=queue.pop(0)
                area.append([x,y])
                if x+1<=len(board)-1:
                    if board[x+1][y]=='O' and visit[x+1][y]==0:
                        queue.append([x+1,y])
                    visit[x+1][y]=1


                if y + 1 <= len(board[0]) - 1:
                    if board[x ][y+1] == 'O' and visit[x ][y+1] == 0:
                        queue.append([x, y+1])
                    visit[x][y+1] = 1
                if y - 1 >=0:
                    if board[x ][y-1] == 'O' and visit[x ][y-1] == 0:
                        queue.append([x, y-1])
                    visit[x][y-1] = 1
                if x - 1 >=0:
                    if board[x-1 ][y] == 'O' and visit[x-1][y] == 0:
                        queue.append([x-1, y])
                    visit[x-1][y] = 1
            for w in area:
                if w[0]==0 or w[0]==len(board)-1 or w[1]==0 or w[1]==len(board[0])-1:
                    fit=False
                    break
            if fit:
                color.extend(area)
        for w in color:
            board[w[0]][w[1]]='X'
        # print(board)


if __name__ == '__main__':
    d=[
        ['X','X','X','X'],
        ['X','O','O','X'],
        ['X','X','O','X'],
        ['X','O','X','X']
    ]
    S=Solution()
    S.solve(d)