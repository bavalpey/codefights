/*
Note: Your solution should have O(n) time complexity, where n is the number of element in l, and O(1) additional space complexity,
since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal
to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end
should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example
  For l = [1, 2, 3, 4, 5] and k = 2, the output should be
    reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
  For l = [1, 2, 3, 4, 5] and k = 1, the output should be
    reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
  For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
    reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
*/
// We can't use recursion, because that violates the O(1) space requirement.
ListNode<int> * reverseNodesInKGroups(ListNode<int> * l, int k) {
  if(k<=1){
    return l;
  }
  int count = 0;
  ListNode<int> *curr = l;
  while(curr != nullptr){
    count++;
    curr = curr->next;
  }
  int numToSwap = count/k;
  int firstNum = numToSwap;
  ListNode<int> *prev = nullptr, *next = nullptr, *start=l, *ans=nullptr, *begin = nullptr;
  curr = l;
  // begin keeps track of the end of the previously reversed list
  // start keeps track of the beginning of the new list to reverse (once reversed, 'start' is the end of the portion
  while(numToSwap>0){
    start = curr; // keep track of the first node
    for(int i = 0; i<k;i++){
      if(i!= k-1){ // this is the standard algorithm to reverse a linked list
        next = curr->next; // temporarily store the next item
        curr->next = prev; // reverse the node
        prev = curr; // now set the previous node to be the current node
        curr = next; // and make curr be the 'next' item
        
      }
      else{ // here is where things change. If we are on the 'last' node to swap, we need to do things differently
        if(numToSwap == firstNum){ // if this is the first time reversing
          begin = start; // I set 'begin' for the first time, this will point to the last item in the list
          ans = curr; // I have to keep track of the first value in the linked list in order to return it at the end
          next = curr->next;
          curr->next = prev;
          curr = next;
          start->next = curr;
        }
        else{
          begin->next = curr; // we need to update what the node right before we started reversing points to
          begin = start; // and update what the new 'last node' is
          next = curr->next; // and also still reverse the node
          curr->next = prev;
          curr = next;
          start->next = curr;
        }
      }
    }
    numToSwap--; // this ensures that we will not start reversing if there are less than k elements in the final reversal
  }
  return ans;
}
