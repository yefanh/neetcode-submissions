class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap: int) -> bool:
            need = 1
            cur = 0
            for w in weights:
                if cur + w > cap:
                    need += 1
                    cur = 0
                cur += w
            return need <= days
        l, r = max(weights) - 1, sum(weights)
        while l + 1 < r:
            m = (l + r) // 2
            if can_ship(m):
                r = m
            else:
                l = m
        return r