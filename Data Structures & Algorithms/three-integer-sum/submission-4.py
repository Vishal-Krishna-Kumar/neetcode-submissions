class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):  # Start from 0
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicates for the first number
            j = i + 1
            k = len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum < 0:
                    j += 1
                elif three_sum > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1  # Skip duplicates for the second number
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1  # Skip duplicates for the third number
        return ans  # Move return outside the loop
