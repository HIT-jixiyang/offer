class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        return self.ishou(sequence)

    def ishou(self, sequence):

        if len(sequence) <= 1:
            return True
        root = sequence[-1]
        for i in range(0, len(sequence) - 1):
            if sequence[i] < root and sequence[i + 1] > root:
                if max(sequence[:i + 1]) > root:
                    return False
                if min(sequence[i + 1:-1]) < root :
                    return False
                else:
                    return self.ishou(sequence[:i + 1]) and self.ishou(sequence[i + 1:-1])
        return True