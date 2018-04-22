"""
Check if all digits of the given integer are even.

Example

  For n = 248622, the output should be
    evenDigitsOnly(n) = true;
  For n = 642386, the output should be
    evenDigitsOnly(n) = false.
"""
def evenDigitsOnly(n)
    n.to_s.each_char do |j|
        unless (j.to_i) % 2 == 0
            return 0
        end
    end
    return 1
end
