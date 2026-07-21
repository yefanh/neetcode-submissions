class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        # dx, dy代表移动方向
        x, y, dx, dy = 0, 0, 1, 0 # y: row, x: col
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."
						# if not in bound or have visited
            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == ".":
                dx, dy = -dy, dx #移动方向顺时针转90度
            
            x += dx
            y += dy
        
        return res