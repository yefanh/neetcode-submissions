class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # idx= 01234567
        # s = "pwwkew"
        #         l 
        #           r 
        substring_set = set()
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in substring_set:
                while s[r] in substring_set:
                    substring_set.remove(s[l])
                    l += 1
                    
            substring_set.add(s[r])
            length = r - l + 1
            res = max(res, length)
        return res

            
