class Solution:
    def reverse(self, x: int) -> int:
       
            
       
        
        d = str(x)
        d = list(d)
        if '-' in d:
            d.remove("-")
            s = '-'
        else:
            s = ""
    
        d.reverse()
        if '0' in d:
            for z in d:
                if z != '0':
                   
                    d = d[d.index(z):]
                    break
                    
                    
                
       
        
        for i in d:
            s+=i
            
        if int(s)>pow(2,31)-1 or int(s)<pow(-2,31):
            return 0;
        return s
        