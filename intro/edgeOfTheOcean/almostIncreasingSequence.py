"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more
than one element from the array.

Example

  For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false;

  There is no one element in this array that can be removed in order to get a strictly increasing sequence.

  For sequence = [1, 3, 2], the output should be
    almostIncreasingSequence(sequence) = true.

  You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly
  increasing sequence [1, 3].
"""
def almostIncreasingSequence(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True
