class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # string valid ? length of window - max(count) <= k to have all elements
        dictionary_word = {}
        l, r = 0, 0
        max_len , max_count = 0, 0
        for r in range(len(s)):
            dictionary_word[s[r]] = 1 + dictionary_word.get(s[r], 0)
            max_count = max(max_count, dictionary_word[s[r]])
            length_of_window = r - l + 1
            if  length_of_window - max_count <= k:
                # valid string with all same chaacter or 2 can change upto less or equal k to equal all tghe string
                max_len = max(max_len, length_of_window)
            else:
                dictionary_word[s[l]] -= 1
                l += 1
        return max_len