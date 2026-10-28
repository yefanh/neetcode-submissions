class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = -1, x + 1
        while l + 1 < r:
            m = (l + r) // 2
            if m * m > x:
                r = m
            else:
                l = m
        return l