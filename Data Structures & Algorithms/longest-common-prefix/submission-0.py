class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float('inf')
        for s in strs:
            length = min(length, len(s))
        ans = ''
        for i in range(length):
            for s in strs:
                if s[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans