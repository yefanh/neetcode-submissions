class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        元素可能存在重复的
        nums = [2,20,4,10,3,4,5]
        nums = []
        nums = [0]
        '''
        num_set = set(nums)
        longest = 0
        
        # if not num_set:
        #     return 0
        if len(num_set) == 1:
            return 1

        for n in nums: # n = -1
            # which means this is the firt element in the sequence
            if (n - 1) not in num_set: 
                length = 1
                while (n + length) in num_set: # 0 in num_set
                    length += 1 # length = 7
                    longest = max(longest, length) # longest = 7
        return longest
