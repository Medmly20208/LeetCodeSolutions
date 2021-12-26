class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = []
        
        count = 0
        if s == "" :
            return 0
        
        if len(s)==1:
            return 1
       
        for i in range(0,len(s)-1):
            l = [s[i]]
            for j in range(i+1,len(s)):
                print(1)
                if s[j] in l:
                    k.append(len(l))
                    break
                    
                else:
                    l.append(s[j])
                    if j == len(s)-1:
                        k.append(len(l))
                
                    
            
       
        return max(k)