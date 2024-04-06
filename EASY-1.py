class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # element : i
        for i,element in enumerate(nums):
          Remainder = target - element
          if (Remainder) in hashmap: # Remainder's indice found
            return [hashmap[Remainder], i] 
          else: 
            hashmap[element] = i # Add element in hashmap