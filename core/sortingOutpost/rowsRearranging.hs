{-
Given a rectangular matrix of integers, check if it is possible to rearrange its rows in such a way that all its columns become strictly
increasing sequences (read from top to bottom).

Example
  For
    matrix = [[2, 7, 1], 
              [0, 2, 0], 
              [1, 3, 1]]
  the output should be
    rowsRearranging(matrix) = false;

  For
    matrix = [[6, 4], 
              [2, 2], 
              [4, 3]]
  the output should be
    rowsRearranging(matrix) = true.
-}

import Data.List
rowsRearranging matrix = isDecreasingFull $ sort matrix
getColumn::[[Int]] -> [Int]
getColumn [[]] = []
getColumn [] = []
getColumn xs = (head $ head xs) : (getColumn $ tail xs)
getTail:: [[Int]] -> [[Int]]
getTail [[]] = []
getTail [] = []
getTail xs = (tail $ head xs) : (getTail $ tail xs)
isDecreasing [] = True
isDecreasing [x] = True
isDecreasing (x:y:zs) = (x < y) && (isDecreasing (y:zs))
isDecreasingFull::[[Int]] -> Bool
isDecreasingFull [[]] = True
isDecreasingFull xs | (length $ head xs) == 1 = isDecreasing $ getColumn xs
                    | otherwise = (isDecreasing $ getColumn xs) && (isDecreasingFull $ getTail xs)
