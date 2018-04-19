/*
Given array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a
smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.

Example

For items = [3, 5, 2, 4, 5], the output should be
  arrayPreviousLess(items) = [-1, 3, -1, 2, 4].
*/
std::vector<int> arrayPreviousLess(std::vector<int> items) {
    std::vector<int> answer;
    for(int i = 0; i < items.size(); ++i ){
        int sub = -1;
        for(int j = 0; j < i;j++){ // for every item in the sub array in i
            if(items[j] < items[i]){sub = items[j];}
        }
        answer.push_back(sub);
    }
    return answer;
}
