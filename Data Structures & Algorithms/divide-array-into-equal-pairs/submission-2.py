class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        array = nums.sort()
        n = len(nums)

        i = 0
        while i < n:
            j = i
            while j < n and nums[i] == nums[j]:
                j += 1
            
            if (j - i) % 2 != 0:
                return False

            i = j  
        return True