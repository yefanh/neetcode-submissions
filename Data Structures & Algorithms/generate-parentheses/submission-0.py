class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [''] * (n * 2)

        def dfs(left:int, right: int) -> None:
            if right == n:
                ans.append(''.join(path))
                return
            if left < n:
                path[left + right] = '('
                dfs(left + 1, right)
            if right < left:
                path[left + right] = ')'
                dfs(left, right + 1)
        dfs(0, 0)
        return ans