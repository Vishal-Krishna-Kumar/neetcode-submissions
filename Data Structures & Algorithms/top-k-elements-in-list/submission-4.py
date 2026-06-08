class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # elements = Counter(nums)
        # ans = sorted(elements.keys(), key=lambda x: elements[x], reverse=True)
        # return ans[:k] -> TC:0(nlogn)
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

        return result[::-1] #(klogn) adding to heap is (logn) and for k element to pop k(logn) so TC: k(logn) in worst case all element are 
        # unique then ask us to give k top ekement and k can be equal to len(arr)

        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]

        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res





