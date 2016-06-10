# EXAMPLE 002
# basic program to compute factorial
#
# compute factorial recursively
# 
def factorial(n):
    if(n == 0):
        return 1;
    else:
        return n*factorial(n-1)
