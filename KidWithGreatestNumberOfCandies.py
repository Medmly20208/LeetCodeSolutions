class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        maxCandi = max(candies)
        
        results = []
        for candie in candies:
            
            if candie+extraCandies >= maxCandi:
                results.append(True)
                
            else:
                results.append(False)
                
                
        return results