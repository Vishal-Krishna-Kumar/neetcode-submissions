class Solution:
    def trap(self, height: List[int]) -> int:
   
        max_l, max_r = [0] * len(height), [0] * len(height)
        max_left, max_right = 0, 0
        for i in range(len(height)):
            max_l[i] = max_left
            max_left = max(max_left, height[i])
# print(max_l)
        for i in range(len(height)-1, -1, -1):
            max_r[i] = max_right
            max_right = max(max_right, height[i])
# print(max_l)
# print(max_r)
        res = 0
        for i in range(len(height)):
            val = min(max_r[i], max_l[i]) - height[i]
            if val < 0:
                val = 0
            res += val
        return res