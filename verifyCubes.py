#
# number theory examples
# EXAMPLE 001
# verify that the sum of the first n cubes is equal to the square of S, where S is the sum of the first n numbers
#
# that is: 
# sigma(1 to n) => S
# sigma(1 to n^3) => S1
#
# To verify that: S*S = S1
#

def verify_until(num_iterations):

    sum_integers = 0
    sum_cubes = 0

    for index in range(num_iterations):
        number = index + 1;
        sum_integers += number;
        sum_cubes += (number*number*number)
        print (str(index+1) + ". SUM OF ALL INTEGERS UNTIL THIS POINT =      " + str(sum_integers) + "; squared = " + str(sum_integers*sum_integers) + " -> " + str(sum_cubes))
        diff = sum_cubes - (sum_integers * sum_integers)
        if(diff != 0):
            print "found an anomaly"
            print (index + 1)
            break;

verify_until(1000);
