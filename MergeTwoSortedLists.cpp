/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {   
        if(l1==NULL && l2==NULL){
            return l1;
        }
        if(l1 == NULL  && l2->next ==NULL ){
            return l2;
        }
        
        if(l2 == NULL  && l1->next ==NULL ){
            return l1;
        }
        if(l1==NULL){
            return l2;
        }
        if(l2==NULL){
            return l1;
        }
        
        ListNode* temp;
        ListNode *stockEnd;
        temp = l1;
        while(temp!=NULL){
        
            stockEnd = temp;
            temp = temp->next;
        }
        
        
       stockEnd->next = l2;
       ListNode*sort = l1;
        ListNode*h = l1;
        int y;
       
       while(!k(h)){
           
           if(sort->next!=NULL){
               if (sort->val>sort->next->val){
                   y = sort->val;
                   sort->val = sort->next->val;
                   sort->next->val = y;
               }
           }
           sort = sort->next;
           if(sort==NULL){
               sort = l1;
           }
           
       }
        
        return l1;
        
        
    }
    
    bool k(ListNode*z){
        
        if(z==NULL || z->next==NULL ){
            return true;
        }
        return (z->val<=z->next->val && k(z->next));
    }
     
        
    
};