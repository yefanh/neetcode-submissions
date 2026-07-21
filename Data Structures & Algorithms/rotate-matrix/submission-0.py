class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # save topleft val
                topLeft = matrix[top][l + i]

                # move botton left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move botton right to botton left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right to botton right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left to top right
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1