class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        board = [[0 for _ in range(cols)] for _ in range(rows)]
        def block(r,c):
            s = sum(map(int,str(r)+str(c)))
            return s>threshold
        self.count=0
        def traverse(r,c):
            if not (0<=r<rows and 0<=c<cols): return
            if board[r][c]!=0: return
            if board[r][c]==-1 or block(r,c):
                board[r][c]=-1
                return
            board[r][c] = 1
            self.count+=1
            traverse(r+1,c)
            traverse(r-1,c)
            traverse(r,c+1)
            traverse(r,c-1)
        traverse(0,0)
        return self.count
