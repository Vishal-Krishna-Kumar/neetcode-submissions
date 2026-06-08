class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1

            else:
                seen.remove(s[l])
                l += 1
        return max_len