class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l= 0
        dictionary_count = {}
        max_count= float('-inf')
        for r in range(len(s)):
            dictionary_count[s[r]] = 1 + dictionary_count.get(s[r], 0)
            max_count = max(max_count, dictionary_count[s[r]])

            length_of_window = r - l + 1
            if length_of_window - max_count <= k:# its valid wimdow
                max_len = max(max_len, length_of_window)
            else:
                dictionary_count[s[l]] -= 1
                l += 1
        return max_len
