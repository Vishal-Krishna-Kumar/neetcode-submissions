class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for c in strs:
            res += str(len(c)) + '#' + c
        return res


    def decode(self, s: str) -> List[str]:
        #42#bfiewbhfoienfoesifnh...
        res , i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # now j would point to '#'
            length = int(s[i : j])
            res.append( s[j+1 : j + 1 + length])
            i = j + 1 + length
        return res