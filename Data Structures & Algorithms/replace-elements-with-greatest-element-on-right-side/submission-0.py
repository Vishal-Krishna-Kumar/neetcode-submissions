class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxEle = -1
        output = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            output[i]=maxEle
            maxEle = max(maxEle, arr[i])
        return output