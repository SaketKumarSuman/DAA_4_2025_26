class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* temp = head;
        
    for(int i=0; i<k ; i++){
        if(temp==NULL) return head;
        temp= temp -> next;
        
    ListNode* prev= NULL;
    ListNode* curr= head;
    ListNode* next= NULL;
        
    for(int i=0; i<k; i++){
        next= curr ->next;
        curr -> next= prev;
        prev=curr;
        curr=next;

        }
    head -> next = reverseKGroup(curr, k);
    return prev;
    }
};

//time complexity = O(n)
//space complexity=O(1)