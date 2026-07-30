import math as m
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def completed_time(value):
            count = 0
            for i in range(len(piles)):
                count += m.ceil(piles[i]/ value)
            return count

        #k minimu how much you will eat que
        low, high = 1, max(piles)
        while low <= high :
            mid = low + (high-low)//2
            limit = completed_time(mid)
            if limit <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low