/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode *ptr = NULL;
    int total = 0, i = 0;
    
    for (ptr = head; ptr != NULL; ptr = ptr->next, total++);
    
    for (ptr = head; ptr != NULL; ptr = ptr->next, i++) {
        if (i == total / 2) {
            return ptr;
        }
    }
    return NULL;
}
