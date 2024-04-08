class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            j = i+1
            k = 1
            number = matrix[0][i]
            while k<m and j<n:
                if matrix[k][j] != number:
                    return False
                k += 1
                j += 1
        for i in range(1, m):
            j = 1
            k = i+1
            number = matrix[i][0]
            while k<m and j<n:
                if matrix[k][j] != number:
                    return False
                k += 1
                j += 1
        return True
