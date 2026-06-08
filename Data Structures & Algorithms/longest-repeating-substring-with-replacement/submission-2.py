class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len, l = 0, 0
        max_count = float('-inf')
       # how to say the staring is valid length of the window - max(count) <= k ok its a valid
        dictionary_count = {}
        
        for r in range(len(s)):
            dictionary_count[s[r]] = 1 + dictionary_count.get(s[r], 0)
            max_count = max(max_count, dictionary_count[s[r]]) # it will give the maximum count
            length_of_window = r - l +1
            if length_of_window - max_count <= k: # its a valid straing
                max_len = max(max_len, length_of_window)
            else:
                dictionary_count[s[l]] -= 1
                l += 1
        return max_len       