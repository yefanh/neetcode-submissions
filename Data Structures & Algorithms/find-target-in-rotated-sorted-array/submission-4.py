class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(i: int) -> bool:
            x = nums[i]
            if x > nums[-1]:
                return target <= x and target > nums[-1]
            return target <= x or target > nums[-1]
        left, right = -1, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right if nums[right] == target else -1