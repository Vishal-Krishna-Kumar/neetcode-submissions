class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_len = float('-inf')
        max_count = 0
        dictionary_count = {}
        while r < len(s):
            # how to say window is valid if u can make all the values to be same 
            # [x, y, x, x, z] = 5 - count(x)[which is maximum] is <=k if s then its valid
            dictionary_count[s[r]] = 1 + dictionary_count.get(s[r], 0)
            max_count = max(max_count, dictionary_count[s[r]])# always the max

            length_of_window = r - l + 1# l and r start at same position even a single element is a window

            if length_of_window - max_count <= k: # then its valid
                max_len = max(max_len, length_of_window)
            else:
                dictionary_count[s[l]] -= 1 # obivious u can remove without checking whether s[l ] in dictionary or not becoz r was take care of that thing
                l += 1
            r += 1
        return max_len