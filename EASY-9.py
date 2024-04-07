class Solution:
    def isPalindrome(self, x: int) -> bool:
      if (x < 0): return False # Skip negative numbers
      Target = x
      ReverseNum = 0
      while (x > 0): 
        ReverseNum *= 10 # Push existing ReverseNum digits left
        ReverseNum += (x % 10) # Add last digit of x to ReverseNum's (which is now 0 due to pushing)
        x//=10 # Floor division x to remove last digit
      return (Target == ReverseNum)
    
'''
Before follow up: 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0): return False # Ignore all negative values
        
        xStr = str(x)
        xLength = len(xStr) - 1
        if (xLength == 0): return True # Ignore all single digit values
        
        center_high = ceil (xLength / 2) # Index of first half
        center_low = floor (xLength / 2) # Index of last half

        FirstHalf =  xStr[0:center_high] # First half of string
        SecondHalf = xStr[-1:center_low:-1] # Second half of string
        
        # print (FirstHalf, SecondHalf)
        return (FirstHalf == SecondHalf)
'''    
