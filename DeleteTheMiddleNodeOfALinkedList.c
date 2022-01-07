/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteMiddle(struct ListNode* head){
    int i = 0,tracker = -1;
    struct ListNode *counter;
    counter = head;
    while(counter!=NULL){
        i+=1;
        counter = counter->next; 
    };

    i = (int) i/2;
      printf("%d",i);
     counter = head;
    if(i==0){
        head = NULL;
    }
    while(counter!=NULL){
        tracker+=1;
        if((i-1)==tracker){
            counter->next = counter->next->next;
            break;
        }
       
        counter = counter->next;
        
    }
    return head;

    
}