"""
Yesterday you found some shoes in the back of your closet. Each shoe is described by two values:

  type indicates if it's a left or a right shoe;
  size is the size of the shoe.
  
Your task is to check whether it is possible to pair the shoes you found in such a way that each pair consists of a right and a left shoe
of an equal size.

Example

  For
    shoes = [[0, 21], 
             [1, 23], 
             [1, 21], 
             [0, 23]]
  the output should be
  pairOfShoes(shoes) = true;

  For
    shoes = [[0, 21], 
             [1, 23], 
             [1, 21], 
             [1, 23]]
  the output should be
  pairOfShoes(shoes) = false.
"""
def pairOfShoes(shoes):
    my_dict = {}
    for i in shoes:
        if i[1] not in my_dict:
            my_dict[i[1]] = [0,0]
        my_dict[i[1]][i[0]] += 1
    for key in my_dict:
        if my_dict[key][0] != my_dict[key][1]:
            return False
    return True
