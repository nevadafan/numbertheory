def an_and_gcd(a, b):
  '''
  Euclid's algorithm for gcd of two numbers
  >>> an_and_gcd(12,4)
  4

  '''
  j, j1 = 1, 0
  k, k1 = 0, 1
  while b:
    q, r = divmod(a,  b)
    a, b = b, r
    j, j1 = j1, j - q * j1
    k, k1 = k1, k - q * k1
  return ((j, k, a) if a > 0 else (-j, -k, -a))
