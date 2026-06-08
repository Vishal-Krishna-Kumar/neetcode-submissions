class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # elements = Counter(nums)
        # ans = sorted(elements.keys(), key=lambda x: elements[x], reverse=True)
        # return ans[:k]
        # min- heap concept
        freq_map = Counter(nums)  
        heap = []  
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))  
            if len(heap) > k: 
                heapq.heappop(heap)  
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])  # Extract elements, ignoring frequency

        return result[::-1] 