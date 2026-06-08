class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = Counter(nums)
        
        # Sort the elements by frequency in descending order
        ans = sorted(elements.keys(), key=lambda x: elements[x], reverse=True)
        
        # Return the top k elements
        return ans[:k]