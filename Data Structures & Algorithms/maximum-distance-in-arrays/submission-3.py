class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Optimized to linear time by keeping track of min and max seen so far
        res = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        n = len(arrays)
        for i in range(1, n):
            array = arrays[i]
            # Calculate distance using current array and the global min/max seen previously
            res = max(res, abs(array[-1] - min_val))
            res = max(res, abs(max_val - array[0]))
            # Update global min/max
            min_val = min(min_val, array[0])
            max_val = max(max_val, array[-1])
        return res