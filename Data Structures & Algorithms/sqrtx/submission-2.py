class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x//2
        if x == 1:
            return 1
        #
        while low <= high:
            mid = low + (high-low)//2#6
            
            print(f'low is {low}')
            print(f'high is {high}')
            print(f'mid is {mid}')

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return high
        