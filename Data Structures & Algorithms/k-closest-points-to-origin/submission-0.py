class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap) # O(n)
        res = []
        while k > 0: # do it until k = 0
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y]) # always append next closet dist points
            k -= 1
        return res

