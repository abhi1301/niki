# Niki
Number of binary string of length 'n' that do not have consecutive 0's

Code is in Python 3

Problem statement: Given an integer 'n', find out total possible bit string (either 0 or 1) of length 'n' which don't have two contiguous zeroes in them. For example if 'n'= 3, then total possible bit strings are 5 {010, 011, 101, 110, 111}.
Since output can be very large, output is modulo 10^9+7.

Code contains 3 approaches (2 commented)

Approach 1: It uses recursion (Divide and conquer approach). But fails if n is very large as it exceeds the maximum recursion depth allowed in Python

Approach 2: It can be seen (from output of approach 1) that the solution to this problem is fibonacci series. nth number of the series is the solution of the of the problem for size n string. Modulo is done at the final output.

Approach 3: It is a modified approach of second one. Performs better that approach 2 because modulo is continuosly done not at the end.

Note: Approach 2 and 3 solve the problem but computation time increases as 'n' becomes larger.
