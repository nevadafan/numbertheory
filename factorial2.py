#
# compute factorial
# with look up table optimization
#
ll1 = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800];

def factorial(n):
    if(n < 0):
        return 1
    if(n <= 10):
        return ll1[n];
    else:
        return n* factorial(n-1);
