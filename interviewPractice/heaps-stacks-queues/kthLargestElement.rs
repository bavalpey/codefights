/*
Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct
element.

Example

  For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
    kthLargestElement(nums, k) = 6;
    
  For nums = [99, 99] and k = 1, the output should be
    kthLargestElement(nums, k) = 99.

*/

use std::collections::BinaryHeap;

fn kthLargestElement(nums: Vec<i32>, k: i32) -> i32 {
  let mut heap = BinaryHeap::from(nums);
  
  
  for i in 0..(k-1) {
    heap.pop().unwrap();
  }
  
  heap.pop().unwrap()
}
