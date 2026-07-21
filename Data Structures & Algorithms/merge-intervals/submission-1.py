class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sweep line algo
        mp = defaultdict(int)
        for start, end in intervals: # O(n)
            mp[start] += 1
            mp[end] -= 1
        res = []
        intervals = []
        have = 0
        for i in sorted(mp):
            if not intervals:
                intervals.append(i)
            have += mp[i]
            if have == 0:
                intervals.append(i)
                res.append(intervals)
                intervals = []
        return res
            


