class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return [seen[diff], index]
            seen[val] = index
            