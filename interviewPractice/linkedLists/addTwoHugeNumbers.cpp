/*
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number
with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the
result in the same format.

Example
  For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
    addTwoHugeNumbers(a, b) = [9876, 5434, 0].
  Explanation: 987654321999 + 18001 = 987654340000.

  For a = [123, 4, 5] and b = [100, 100, 100], the output should be
    addTwoHugeNumbers(a, b) = [223, 104, 105].
  Explanation: 12300040005 + 10001000100 = 22301040105.
*/

// Definition for singly-linked list:
// template<typename T>
// struct ListNode {
//   ListNode(const T &v) : value(v), next(nullptr) {}
//   T value;
//   ListNode *next;
// };
//
#include <stack>
void addNode(struct ListNode<int> *&head, int n){
  struct ListNode<int> *NewNode = new ListNode(0);
  NewNode-> value = n;
  NewNode -> next = head;
  head = NewNode;
}
ListNode<int> * addTwoHugeNumbers(ListNode<int> * a, ListNode<int> * b) {
  if(b == nullptr)return a;
  else if(a == nullptr)return b;
  std::stack<int> astack;
  std::stack<int> bstack;
  std::stack<int> sumstack;
  ListNode<int> * curr = a;
  while(curr != nullptr){
    astack.push(curr->value);
    curr = curr->next;
  }
  curr = b;
  while(curr != nullptr){
    bstack.push(curr->value);
    curr = curr->next;
  }
  int carry = 0;
  int bval = 0;
  int aval = 0;
  int sumval = 0;
  ListNode<int> * val = nullptr;
  while((!astack.empty()) or (!bstack.empty())){
    if(!astack.empty()){
      aval = astack.top();
      astack.pop();
    } else aval = 0;
    if(!bstack.empty()){
      bval = bstack.top();
      bstack.pop();
    } else bval = 0;
    sumval = (int) (aval + bval + carry) % 10000;
    addNode(val,sumval);
    carry = (aval + bval + carry) > 9999;
  }
  if(carry != 0){
    addNode(val,carry);
  }
  return val;
}
