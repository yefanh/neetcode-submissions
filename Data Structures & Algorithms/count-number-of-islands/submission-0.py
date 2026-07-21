class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit = set()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c)) # [(r,c)] -> append tuple in deque 
            while q:
                row, col = q.popleft()
                direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in direction:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and 
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
                    
        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == '1' and (row, col) not in visit):
                    bfs(row, col)
                    islands += 1
        return islands