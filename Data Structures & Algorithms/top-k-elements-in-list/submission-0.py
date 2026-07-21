class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # insert a tuple (number of num, num) into heap
            if len(heap) > k:
                heapq.heappop(heap)
        # [(top k (number of num, num))] return only [top k num]
        res = []
        for i in range(len(heap)):
            res.append(heap[i][1])
        return res


            
        

            
