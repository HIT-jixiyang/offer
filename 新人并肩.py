class Solution(object):
    def minchangesWs(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n_change = 0
        position = {x: i for (i, x) in enumerate(row)}
        n = len(row)
        for i in range(0, n, 2):
            x = row[i]
            if x % 2 == 0:
                y = x + 1
            else:
                y = x - 1
            j = position[y]

            if abs(i - j) > 1:
                row[i + 1], row[j] = row[j], row[i + 1]
                position[row[i + 1]], position[row[j]] = i + 1, j
                n_change += 1

        return n_change
if __name__ == '__main__':
    n=int(input())
    row=list(map(int,input().strip().split(' ')))
    S=Solution()
    print(S.minchangesWs(row))