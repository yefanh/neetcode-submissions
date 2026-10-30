class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        end = len(nums) - 1
        while end > 0 and nums[0] == nums[end]:
            end -= 1
        last = nums[end]

        def check(i: int) -> bool:
            x = nums[i]
            if x > last:
                return target <= x and target > last
            return target <= x or target > last
        
        l, r = -1, end
        while l + 1 < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        return nums[r] == target