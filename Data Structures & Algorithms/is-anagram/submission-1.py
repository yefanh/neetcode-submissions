class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = collections.defaultdict(int)
        countT = collections.defaultdict(int)
        for char in s:
            countS[char] += 1
        #     print(countS)
        # print('-')
        for char in t:
            countT[char] += 1
           
            # print(countS)
        
        return countS == countT
            
