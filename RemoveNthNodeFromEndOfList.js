/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let k = head
    let counter = 0
    
    while(k!=null){
        k = k.next;
        counter+=1
    }
    if(counter==1 && n==1){
        return null
    }
    
    counter =counter-n+1
    
    let tracker = 0;
    let previous = head ;
    k = head;
   
    while(k!=null){
        tracker+=1
        if(tracker===counter && counter===1){
            head = k.next;
            break
        }
         if(tracker===counter){
            console.log(true)  
            previous.next = k.next
            break
        }
        previous = k
        k = k.next
        
    }
   return head
};