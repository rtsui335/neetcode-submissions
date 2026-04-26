class Solution:
    def check(self, nums: List[int]) -> bool:
        #make a sorted copy of input array
        array = sorted(nums)
        arr = []
        #for every rotation, compare and check elements from sorted to original
        #if matches, returnt true else return false
        for i in range(len(nums)):
            arr.insert(0, array.pop())
            if nums == arr + array:
                return True
        
        return False