# finition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

            
class Solution:
    def addTwoNumbers(self, l1, l2):
        d = l1
        su = 0
        s1 = ""
        while d!=None:
            
            s1+=(str(d.val))
            d = d.next
        s1 = s1[::-1]  
        s1 = int(s1)
        
        d = l2
        s2 = ""
        while d!=None:
            
            s2+=(str(d.val))
            d = d.next
        
        s2 = s2[::-1] 
        s2 = int(s2)
        
        sumof = s1+s2
        
        sumof = str(sumof)[::-1]
        h = ListNode(sumof[0],None)
        l3 = h
        for j in range(1,len(sumof)):
            h.next = ListNode(sumof[j],None)
            h = h.next
            
            
            
        return l3
        
            
    
        
        
        
        
        
        
        