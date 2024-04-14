class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      Tc = 0
      rem_arr = []
      
      for i in range (0,len(nums)):
        if (nums[i] == val): 
          Tc+=1
          rem_arr.append(i)
      
      for i in range (0,Tc):
        nums.pop(rem_arr[i]-i)
      
      return len(nums)