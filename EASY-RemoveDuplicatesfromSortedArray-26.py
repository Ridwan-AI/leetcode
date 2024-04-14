class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Start from the back of the array as .pop() is faster than .remove()
        CurrentIndex = len(nums) - 1
        while CurrentIndex != 0:
            if (nums[CurrentIndex] == nums[CurrentIndex-1]): 
              nums.pop(CurrentIndex)
            CurrentIndex -= 1
            # print(nums, CurI)
        return len(nums)
