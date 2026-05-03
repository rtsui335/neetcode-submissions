class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        #sort the array 
        #return the difference between  product of first last and two elements
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]