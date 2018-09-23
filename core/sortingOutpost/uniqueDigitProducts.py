"""
Let's call product(x) the product of x's digits. Given an array of integers a, calculate product(x) for each x in a, and return the
number of distinct results you get.

Example
For a = [2, 8, 121, 42, 222, 23], the output should be
  uniqueDigitProducts(a) = 3.

Here are the products of the array's elements:

2: product(2) = 2;
8: product(8) = 8;
121: product(121) = 1 * 2 * 1 = 2;
42: product(42) = 4 * 2 = 8;
222: product(222) = 2 * 2 * 2 = 8;
23: product(23) = 2 * 3 = 6.
As you can see, there are only 3 different products: 2, 6 and 8.
"""
def uniqueDigitProducts(a):
  j = list(map(lambda x: [int(i) for i in str(x)] + [1], a))
  i = lambda f: functools.reduce(lambda x,y: x*y,f)
  return len(set(map(i,j)))
