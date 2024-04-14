class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Since the majority is always more than half of the total numbers, post-sorting, median's the majority
        nums.sort()
        n = len(nums)
        return nums[n//2]
