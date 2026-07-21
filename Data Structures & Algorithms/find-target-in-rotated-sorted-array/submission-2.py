class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]: # left sorted portion， must have '=', eg,[1, 3], mid = 1
                if target > nums[mid] or target < nums[l]: # go right
                    l = mid + 1
                else: # target <= nums[mid] and target >= nums[l], go left
                    r = mid - 1
            else: # right portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
