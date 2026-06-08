class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        min_val = arr[0]
        max_profit = 0
        for i in range(len(arr)):
            profit = arr[i] - min_val
            max_profit = max(max_profit, profit)
            min_val = min(min_val, arr[i])  
        return max_profit