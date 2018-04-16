"""
We define the weakness of number x as the number of positive integers smaller than x that have more divisors than x.

It follows that the weaker the number, the greater overall weakness it has. For the given integer n, you need to answer two questions:
  what is the weakness of the weakest numbers in the range [1, n]?
  how many numbers in the range [1, n] have this weakness?
  
Return the answer as an array of two elements, where the first element is the answer to the first question, and the second element is
the answer to the second question.

Example

For n = 9, the output should be
weakNumbers(n) = [2, 2].

Here are the number of divisors and the specific weakness of each number in range [1, 9]:
  1: d(1) = 1, weakness(1) = 0;
  2: d(2) = 2, weakness(2) = 0;
  3: d(3) = 2, weakness(3) = 0;
  4: d(4) = 3, weakness(4) = 0;
  5: d(5) = 2, weakness(5) = 1;
  6: d(6) = 4, weakness(6) = 0;
  7: d(7) = 2, weakness(7) = 2;
  8: d(8) = 4, weakness(8) = 0;
  9: d(9) = 3, weakness(9) = 2.
As you can see, the maximal weakness is 2, and there are 2 numbers with that weakness level.
"""
def divisors(n):
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            if not i in factors:
                factors[i] = 0
            factors[i] += 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    for factor in generate(0):
        yield factor
        
def weakness(x):
    return len(list(divisors(x)))

def weakNumbers(n):
    divisors_map = list(map(weakness, range(1,n+1)))
    maximum = 0
    weakness_map = [0]*n
    num = 0
    for i in range(1,len(divisors_map)):
        if not divisors_map[i] > max(divisors_map[:i]):
            count = 0
            for x in divisors_map[:i]:
                if x > divisors_map[i]:
                    count += 1
            if count == maximum:
                num += 1
            elif count > maximum:
                num = 1
                maximum = count
    if maximum == 0:
        return [0,n]
    return [maximum,num]
    
