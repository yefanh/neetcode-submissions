class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        left, right = -1, r * c
        while left + 1 < right:
            mid = (left + right) // 2
            x = matrix[mid // c][mid % c]
            if target == x:
                return True
            if x < target:
                left = mid
            else:
                right = mid
        return False