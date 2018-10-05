/*
DESCRIPTION FOR THIS PROBLEM IS BELOW CODE DUE TO ITS LENGTH
*/
bool hasNoChildren(Tree<int> * node){
  return (node->left == nullptr && node->right == nullptr);
}
bool isNodeSymmetric(Tree<int> * right, Tree<int> * left){
  if(right == nullptr && left == nullptr) return true;
  else if(right == nullptr || left == nullptr) return false;
  else if(hasNoChildren(left) && hasNoChildren(right)) return left->value == right->value;
  else return left->value == right->value && isNodeSymmetric(left->right,right->left) && isNodeSymmetric(left->left,right->right);
}
bool isTreeSymmetric(Tree<int> * t) {
  if(t==nullptr) return true;
  return isNodeSymmetric(t->right,t->left);
}


/*
Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

Example
  For
    t = {
        "value": 1,
        "left": {
            "value": 2,
            "left": {
                "value": 3,
                "left": null,
                "right": null
            },
            "right": {
                "value": 4,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 2,
            "left": {
                "value": 4,
                "left": null,
                "right": null
            },
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        }
    }
  the output should be isTreeSymmetric(t) = true.
  Here's what the tree in this example looks like:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
  As you can see, it is symmetric.

  For
    t = {
        "value": 1,
        "left": {
            "value": 2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        }
    }
  the output should be isTreeSymmetric(t) = false.
  Here's what the tree in this example looks like:
        1
       / \
      2   2
       \   \
       3    3
  As you can see, it is not symmetric.
*/
