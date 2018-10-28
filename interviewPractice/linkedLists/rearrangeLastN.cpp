/*
Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example
  For l = [1, 2, 3, 4, 5] and n = 3, the output should be
    rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
  For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
    rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].
*/

ListNode<int> * rearrangeLastN(ListNode<int> * l, int n) {
  // start by getting the size of the list
  if(n == 0) return l;
  ListNode<int> *curr = l;
  int count = 0;
  while(curr != nullptr){
    count++;
    curr = curr->next;
  }
  if(count == n){
    return l;
  }
  // once we have this, all we need to do is remove the arrow pointing to the first one to move
  // and make the old 'last' node point to the beginning
  int goal = count - n;
  int curCount = 0;
  curr = l;
  ListNode<int> *next = nullptr, *ans = nullptr, *prev = nullptr;
  while(curr!=nullptr){
    curCount++;
    if(curCount == goal+1){
      if(curr->next == nullptr){
        prev->next = nullptr;
        curr->next = l;
        return curr;
      }
      ans=curr;
      next = curr->next;
      prev->next = nullptr;
      curr = next;
    }
    if(curr->next == nullptr || curr == nullptr){
      curr->next = l;
      return ans;
    }
    else{
      prev = curr;
      curr = curr->next;
    }
  }
  return ans;
}
