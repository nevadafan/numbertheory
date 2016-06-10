def an_and_gcd(a, b):
  '''
  Euclid's algorithm for gcd

  '''
  u, u1 = 1, 0
  v, v1 = 0, 1
  while b:
    q, r = divmod(a,  b)
    a, b = b, r
    u, u1 = u1, u - q * u1
    v, v1 = v1, v - q * v1
  return (u, v, a) if a > 0 else (-u, -v, -a)
