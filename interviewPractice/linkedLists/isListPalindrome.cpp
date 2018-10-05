/*
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is
what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Example
  For l = [0, 1, 0], the output should be
    isListPalindrome(l) = true;
  For l = [1, 2, 2, 3], the output should be
    isListPalindrome(l) = false.
*/

// Definition for singly-linked list:
// template<typename T>
// struct ListNode {
//   ListNode(const T &v) : value(v), next(nullptr) {}
//   T value;
//   ListNode *next;
// };
//
bool isListPalindrome(ListNode<int> * l) {
  // This should work in O(2.5n)
  if(l == nullptr || l->next == nullptr){ // account for lists of size 0 or 1
    return true;
  }else if(l->next->next == nullptr){ // account for lists of size 2
    return l->value == l->next->value;
  }else if(l->next->next->next == nullptr){ // account for lists of size 3
    return l->value == l->next->next->value;
  }
  int size = 0; // counter 
  ListNode<int>*curr = l;
  while(curr != nullptr){
    curr = curr->next;
    size++;}
  ListNode<int> * prev=nullptr, *next = nullptr;
  curr = l;
  int midPt = size/2;
  ListNode<int> * midPointer = nullptr;
  for(int i =0;i<=midPt;i++){ // this for loop will reverse the first half of the linked list
    if(i!=midPt){ // if we are at the midpoint, we need to do something special
      next = curr->next; // next is a temp value that refers to the next node that needs to be modified.
      curr->next = prev; // we want to reverse the list, so make the curr node point to the previous
      prev = curr;       // set the previous to be the current
      curr = next;       // and now set the current to be the next node
    }else{
      l = prev; // If we are at the midpoint, we want the 'head' of the first half of the list to be the final node
      midPointer = curr; // and we want the mid to be the current node.
    }
  }
  if(size%2){ // if the length of the list is odd, we want to skip the middle element.
    midPointer = midPointer->next;
  }
  ListNode<int> *curr2 = midPointer;

  
  while(l != nullptr){ // now, check if the reversed first half is equivalent to the second half
    if(l->value != midPointer->value){
      return false;
    }
    l = l->next;
    midPointer = midPointer->next;
  }
  return true;
  

}
