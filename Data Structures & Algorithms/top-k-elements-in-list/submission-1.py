class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # {1:1, 2:2, 3:3}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # # of count at most len(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        # buckets = [[], [], [2], [3], [], [], []]
        for num in count.keys():
            buckets[count[num]].append(num)
        
        # [2, 3]
        res = []
        for i in range(len(buckets)-1, -1, -1):
            if not buckets[i]:
                continue
            else:
                res.extend(buckets[i])
                if len(res) == k:
                    return res
                    
            



            
        

            
