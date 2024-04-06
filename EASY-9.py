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