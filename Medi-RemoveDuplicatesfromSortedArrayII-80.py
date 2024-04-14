class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        repitions = list(Counter(nums).values())
        values = list(Counter(nums).keys())

        for i,e in enumerate (values):
          for j in range (2,repitions[i]):
            nums.remove(e)
        return len(nums)