

'''
def isAnagramIn(TestStr, AnagramArray) -> bool:
  FoundIndex = -1
  for i,AnagramFirstElement in enumerate (AnagramArray):
    if (sorted(TestStr) == sorted(AnagramFirstElement[0])):
      FoundIndex = i
  return FoundIndex 

class Solution:
    def groupAnagrams(self, strs):
      FoundAnagrams = [[strs[0]]]
      
      # Find anagrams
      for TestStr in (strs[1:]):
        FoundIndex = isAnagramIn (TestStr, FoundAnagrams)
        if (FoundIndex != -1): # Found
          FoundAnagrams[FoundIndex] += [TestStr]
        else: # Not found
          FoundAnagrams += [[TestStr]]

      return (FoundAnagrams)
'''