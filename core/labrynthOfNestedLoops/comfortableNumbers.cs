/*
Let's say that number a feels comfortable with number b if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.

How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [l, r], and each number feels comfortable with the other?

Example

For l = 10 and r = 12, the output should be
  comfortableNumbers(l, r) = 2.

Here are all values of s(x) to consider:

  s(10) = 1, so 10 is comfortable with 9 and 11;
  s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
  s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.
  Thus, there are 2 pairs of numbers comfortable with each other within the segment [10; 12]: (10, 11) and (11, 12).
*/
int comfortableNumbers(int L, int R) {
    if(L==R)
        return 0;
 
    int a = L, b = a + 1, sumA = 0, pairs = 0;
    List<string> listPairs = new List<string>();
    while (a < R) {
        string aStr = a.ToString();
        int aX = 0;
 
        while (aX < aStr.Length) {
            sumA = sumA + int.Parse(aStr[aX]+"");
            aX = aX + 1;
        }
        while (b <= R) {
            string bStr = b.ToString();
            int bX = 0, sumB = 0;
 
            while (bX < bStr.Length) {
                sumB = sumB + int.Parse(bStr[bX]+"");
                bX = bX + 1;
            }
 
            if((b >= a - sumA) && (b <= a + sumA)&&
              (a >= b - sumB) && (a <= b + sumB)) {
                pairs = pairs + 1;
            }
 
            b = b + 1;
        }
 
        a = a + 1;
        b = a + 1;
        sumA = 0;
    }
    return pairs;
}
