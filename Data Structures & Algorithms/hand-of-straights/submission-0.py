class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: # non 0 means True in python
            return False
        count = {}

        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                # {1:2, 2:1, 3:2}, i = 2, second round.
                if count[i] == 0: #count[2] == 0
                    if i != minH[0]: # 2 != 1(2 not equal to min val)
                        return False 
                    heapq.heappop(minH)
        return True