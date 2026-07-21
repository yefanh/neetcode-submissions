class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-2,1,-3,4,-1,2,1,-5,4]
        '''
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(curSum, maxSub)
        return maxSub
                