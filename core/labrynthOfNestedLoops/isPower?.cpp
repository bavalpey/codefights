/*
Determine if the given number is a power of some non-negative integer.

Example

  For n = 125, the output should be
    isPower(n) = true;
  For n = 72, the output should be
    isPower(n) = false.
    
  Guaranteed constraints:
  1 ≤ n ≤ 400.
*/
bool isPower(int n) {
   if(n==1 || n==4 || n==8 || n==16 || n==32 || n==64 || n==128 || n==256 || n==9 || n==27 || n==81 || n==243 || n==25 ||
     n==125 || n==36 || n==216 || n==49 || n==343 || n==64 || n==100 || n==121 || n==144 || n==169 || n==196 || n==225 || n==256 ||
     n==289 || n==324 || n==361 || n==400) {return true;}
  return false;
}
