/*
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an
interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list,
also sorted in non-decreasing order, that contains the elements from both original lists.

Example
  For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
    mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
  For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
    mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
*/
ListNode<int> * mergeTwoLinkedLists(ListNode<int> * l1, ListNode<int> * l2) {
  if(l1 == nullptr) return l2;
  if(l2 == nullptr) return l1;
  stack<int> s;
  int l1v, l2v;
  ListNode<int> *head = nullptr;
  while(l1 != nullptr || l2!=nullptr){
    
    if(l1 == nullptr) l1v = INT_MAX;
    else l1v = l1->value;
    if(l2 == nullptr) l2v = INT_MAX;
    else l2v = l2->value;
    if(l2v < l1v) l2 = l2->next;
    else l1 = l1->next;
    s.push(std::min({l1v,l2v}));
  }
  while(!s.empty()){
    addNode(head,s.top());
    s.pop();
  }
  return head;
}
