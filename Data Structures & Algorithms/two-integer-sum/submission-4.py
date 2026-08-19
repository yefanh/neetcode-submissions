class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3,4,5,6], target = 7

        preMap = {} # key: n, val: index
        for i, n in enumerate(nums):
            diff = target - n # diff = 4, 3
            if diff in preMap:
                return [preMap[diff], i] # [0, 1]
            preMap[n] = i # preMap = {3:0}