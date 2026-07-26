class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dictionary = defaultdict(list)
        # a a a a a 
        '''
        h : [0, 2, 4]
        o : [1, 3, 5]

        '''
        for i in range(len(s)):
            dictionary[s[i]].append(i)
        max_len = -1
        for key, val in dictionary.items():
            if len(val)>1:
                length = (val[-1] - val[0])-1
                max_len = max(length, max_len)
        return max_len