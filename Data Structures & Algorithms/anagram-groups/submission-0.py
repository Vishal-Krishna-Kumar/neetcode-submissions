class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs: # every stirng of character conunt the value occur
            count = [0] * 26
            for c in s: # individual character in a string
                idx = ord(c) - ord('a') # 99 - 97 -> c- a
                count[idx] += 1
            key = tuple(count) # why becoz count is a list so key should be unique in dictionary
            if key not in seen:
                seen[key] = [s]
            else:
                seen[key].append(s)
        return seen.values()