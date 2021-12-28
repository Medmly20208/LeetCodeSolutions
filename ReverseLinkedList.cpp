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
    ListNode* reverseList(ListNode* head) {
            ListNode *prev, *curr, *stock_next = NULL, *s;
    curr = head;
    while (curr != NULL)
    {

      s = curr;
      curr = curr->next;
      s->next = stock_next;
      stock_next = s;
      head = s;
    }
      return head;
    }
};
