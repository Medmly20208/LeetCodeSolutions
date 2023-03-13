class Solution:
    def isHappy(self, n: int) -> bool:
        nb = str(n)
        
        result = 0
        
        for i in nb:
            result = result+ pow(int(i),2)
            
        
        
        visited = []
        
        
        while True:
            
            s = str(result)
            
            
            
            result =0
            for i in s:
                result = result + pow(int(i),2)
                
            if result in visited:
                return False
            
                
            if result==1:
                return True
            
            else:
                visited.append(result)