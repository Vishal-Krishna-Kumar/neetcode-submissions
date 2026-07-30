class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def maximumWeight(value):#10
            howManyDays = 1
            count = 0
            for w in weights:
                if count + w > value:
                    howManyDays += 1#2
                    count = 0
                count += w
            print(f'the value of mid :{mid}')
            print(f'How many days: {howManyDays}')
            return howManyDays


        low, high = max(weights), sum(weights)
        #1, 10
        while low <= high:
            mid = low + (high-low)//2
            limit = maximumWeight(mid)
            if limit <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low