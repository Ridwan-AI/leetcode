class Solution:
    def romanToInt(self, s: str) -> int:
      RomanKeyChar = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
      }
      FinalNum = 0
      for i,element in enumerate(s):
        if (i+1) == len(s): FinalNum += RomanKeyChar[element]
        elif (RomanKeyChar[s[i]] >= RomanKeyChar[s[i+1]]): FinalNum += RomanKeyChar[element]
        else: FinalNum -= RomanKeyChar[element]

      return FinalNum