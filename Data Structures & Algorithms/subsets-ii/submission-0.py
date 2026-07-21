class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return

            x = nums[i]
            path.append(x)
            dfs(i + 1)
            path.pop()

            i += 1
            while i < n and nums[i] == x:
                i += 1
            dfs(i)
        dfs(0)
        return ans