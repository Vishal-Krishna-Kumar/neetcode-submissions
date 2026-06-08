class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0
        for i in nums:
            if i - 1 not in seen: # then i is the first element
                length = 0
                while i + length in seen:
                    length += 1
                max_len = max(max_len, length)
        return max_len