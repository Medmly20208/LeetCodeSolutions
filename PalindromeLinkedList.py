# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        p = []
        d = head
        while d!=None:
            l.append(d.val)
            p.append(d.val)
            d = d.next
    
        l.reverse()   
       
        return l == p
        
        