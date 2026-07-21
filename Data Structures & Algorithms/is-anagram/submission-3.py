class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        for char in s:
            countS[char] = countS.get(char, 0) + 1
        #     print(countS)
        # print('-')
        for char in t:
            countT[char] = countT.get(char, 0) + 1
           
            # print(countS)
        
        return countS == countT
            
