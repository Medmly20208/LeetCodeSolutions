class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x = str(x)
      
        origin = list(x)
        d = list(x)
        d.reverse()
        if origin == d:
            return True
        else:
            return False