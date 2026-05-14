class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #brute force
        n = len(nums)
        for i in range(0, n - 1):
            for j in range(i + 1, min(len(nums), i + k + 1)):
                if nums[i] == nums[j]:
                    return True
        return False