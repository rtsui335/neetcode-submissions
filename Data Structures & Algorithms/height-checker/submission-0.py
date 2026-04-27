class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #create sorted copy and counter to 0
        length = sorted(heights)
        result = 0

        #iterate through both arrays and if the original differs, increment result
        for i in range(len(heights)):
            if heights[i] != length[i]:
                result += 1
        return result
        