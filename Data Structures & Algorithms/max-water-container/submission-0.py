class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while l < r:
            # 2 .... 7 the water can hold upto 2
            ans = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, ans)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_area