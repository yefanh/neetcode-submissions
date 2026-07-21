class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
         0, 1, 2, 3
        [1, 2, 4, 6]nums
        prefix=[1, 2, 8, 32]
        posfix=[48, 48, 24, 6]
        [1, 1, 2, 8]res
        [48, 24, 12, 8]res
        '''
        res = [1] * len(nums)
        for i in range(len(nums)-1):# i = 0, 1, 2 i = 2
            res[i+1] = res[i] * nums[i] #res[3] = res[2] * nums[2] = 2, res=[1,1,2,8]

        posfix = 1
        for i in range(len(nums)-2, -1, -1):# i=2,1 i = 2
            posfix *= nums[i+1] #postfix = 1*6 =6
            res[i] = res[i] * posfix # res[2] = 2*6=12
        return res
        


