# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        
        l = head
        i=0
        while l!=None:
            i+=1
            
            if i%2==0:
                odd.append(l.val)
            else:
                even.append(l.val)
                
            l = l.next
            
        print(odd)
        print(even)
        odd = even+odd
        print(odd)
        l=head
        j = 0
        while l!=None:
            l.val = odd[j]
            j+=1
            l = l.next
            
            
            
        return head
            
            
            
            
            
        