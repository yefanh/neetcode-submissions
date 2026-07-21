class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        string = ''
        for s in strs:
            string += str(len(s)) + '#' + s
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        [wordaderv3]len = 12 -> two digits
        12#word
        [0]
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # 10#hellohello5#world
            res.append(s[j+1:j+1+length])
            i = j + 1 + length

        return res


        
            




            
            
            



