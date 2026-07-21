class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for n in strs:
            count = [0] * 26
            for c in n:
                num = ord(c) - ord('a') 
                count[num] += 1
            res[tuple(count)].append(n)
        return list(res.values())
                
                