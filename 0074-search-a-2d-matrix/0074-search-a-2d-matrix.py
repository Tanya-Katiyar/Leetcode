class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag=False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(target == matrix[i][j]):
                    flag=True
        return flag
