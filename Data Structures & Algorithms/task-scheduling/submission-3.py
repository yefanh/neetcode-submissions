class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #O(n)
        maxHeap = [-cnt for cnt in count.values()] #O(m)
        heapq.heapify(maxHeap)# minheap, since all nums are "-" so it is maxHeap # O(m)
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            # if no task in maxheap, but task in queue, then jump to the time of 1st element
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt: # if cnt is not 0
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
