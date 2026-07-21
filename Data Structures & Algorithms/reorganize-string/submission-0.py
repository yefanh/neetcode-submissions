class Solution:
    def reorganizeString(self, s: str) -> str:
        # s = abasddasw
        # s = aaaaab
        # s = "aab"
        count = Counter(s) # {'a': 2, 'b': 1}
        max_heap = []
        for s, c in count.items():
            max_heap.append([-c, s]) # [[-2, 'a'], [-1, 'b'], ...]
        heapq.heapify(max_heap) # O(n) rank the count, minheap

        # initial
        res = ''
        prev = None # store the char that have already added, avoid repetition

        while max_heap or prev:
            if prev and not max_heap:
                return ''
                
            cnt, char = heapq.heappop(max_heap) # cnt is negative
            res += char
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None # !!!!
            
            if cnt != 0:
                prev = [cnt, char]
        return res




            
            
