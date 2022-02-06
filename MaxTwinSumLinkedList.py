# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        j = head
        l = []
        while j!=None:
            l.append(j.val)
            j = j.next
            
        maxes = []
        o = len(l)-1
        for i in range(0,int(len(l)/2)):
            u = l[i]+l[o]
            maxes.append(u)
            o = o-1
            
        return max(maxes)
                
        
        