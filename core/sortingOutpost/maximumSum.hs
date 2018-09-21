{-
You are given an array of integers a. A range sum query is defined by a pair of non-negative integers l and r (l <= r). The output to a
range sum query on the given array a is the sum of all the elements of a that have indices from l to r, inclusive.

You have the array a and a list of range sum queries q. Find an algorithm that can rearrange the array a in such a way that the total
sum of all of the query outputs is maximized, and return this total sum.

Example

For a = [9, 7, 2, 4, 4] and q = [[1, 3], [1, 4], [0, 2]], the output should be
  maximumSum(a, q) = 62.

You can get this sum if the array a is rearranged to be [2, 9, 7, 4, 4]. In that case, the first range sum query [1, 3] returns the sum
9 + 7 + 4 = 20, the second query [1, 4] returns the sum 9 + 7 + 4 + 4 = 24, and the third query [0, 2] returns the sum 2 + 9 + 7 = 18.
The total sum will be 20 + 24 + 18 = 62.
-}

import Data.List -- This library contains the sort function
maximumSum :: [Int] -> [[Int]] -> Int -- This declares the type structure of the function. Namely, it takes a list of ints and
                                      -- a list of lists of ints and returns an Int
maximumSum a q = 
          sum $ zipWith (*) (reverse $ sort a) (reverse . sort . count $ convergeArray q)
          
          {- convergeArray will convert the 2d list q into a single list consisting of all of the indices in each range.
          in other words, convergeArray([1,2],[0,2]) produces [1,2,0,1,2].
          then, we want to count the frequency of each index, because this tells us how to order the array to maximize the sum
          After we have computed this, we want to determine the maximal sum.  Instead of having to map out the counts to the
          indices, we can just sort the counted list of indices (losing the index in the process), but also sort the first list
          so that the largest element is first, and the count of the most frequently occuring index comes first. (if we did not
          sort ascending, if not every index appears in the indiecs that are summed, the maximal sum would not be computed)
          To conduct elementwise multiplication in Haskell, use zipWith (*). (Actually, zipWith will combine two lists into one
          list, where the combination is whichever function is passed as the first argument).
          Finally, we compute the sum of the resulting list.
          -}
convergeArray :: [[Int]] -> [Int]
convergeArray [] = []
convergeArray x = [head $ head x .. last $ head x] ++ (convergeArray $ tail x)
count s = map (\x -> (length x)) . group . sort $ s
{- count utilizes map, which applies a function to each element of a list.  We then pass in an inline function using ' \x -> ' which is
exactly the same thing as python's ' lambda x: ' notation.  First, we sort s so that the same elements are paired together. Then,
we use the group function. The group function will create a list of lists that, if each element were to be concatenated, would result
in the original list. (i.e. group [1,1,1,3,3] results in [[1,1,1],[3,3]]). In this form, we can map the list to count the length of
each group to find that index's frequency.
-}

{- Note on the use of '$' and '.'
Both $ and . work with nested functions.  Because arguments of functions are passed in separated by spaces (as opposed to commas, such
as in python) and are not necessarily surrounded by parenthesis, any 'word' after a function name is passed in as an argument.  This
means that, if you write sum tail [1,2,3], it will not work as sum(tail [1,2,3]).  Instead, it would try to pass in 'tail' as an
argument to sum, which of course does not work.  Using $ or really just says to evaluate what comes after before using it as an
argument.  So sum $ tail [1,2,3] is the same thing as calling sum (tail [1,2,3]). The use of the "." (dot) is to nest functions, which
means that if you use . to preceed something, there must be an argument that comes after it, so the last function
in a series of nested functions must end with $, as seen in line 22 with reverse . sort . count $ convergeArray q, which really just
reads as reverse (sort (count ( convergeArray q))), but looks nicer.
-}
