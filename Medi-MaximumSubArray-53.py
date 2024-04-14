class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      Max_SoFar = nums[0] # Set to first num in array
      CurrentSum = 0

      for num in nums:
        if CurrentSum < 0: CurrentSum = 0 # Reset if previous number was negative, as an array full of negative numbers would be the sum of the smallest negative number
        CurrentSum += num
        Max_SoFar = max(Max_SoFar, CurrentSum) # Update Max_SoFar to be the largest of the two
      return Max_SoFar

