'''
Finding number of binary string of length 'n' that do not have consecutive 0's
'''

from math import pow, sqrt
'''
# Approach 1: Recursion : Divide nad conquer
Problem : Cannot solve for very large n as number of maximum recursion depth is exceeded.

def count01(n, lastDigit):

    if n== 1:
        if lastDigit == 1:
            return 2
        else:
            return 1

    if lastDigit == 1:
        return (count01(n-1, 0) + count01(n-1, 1))
    elif lastDigit == 0:
        return count01(n-1, 1)
'''
# Solution to the given problem forms a fibonacci number (can be seen from the output of approach 1)
# So next two approaches are nth fibonacci number generator : solution to the problem..

'''
# Approach 2: Iteration method
Problem: Takes more time as the n becomes larger.

def count02(n):
    num0 = 1
    num1 = 1
    i = 0
    while i < n:
        out = (num0 + num1)
        num0 = num1
        num1 = out
        i += 1

    return num1

'''

'''
# Approach 3: Iteration method  (MODIFIED APPROACH 2)
Problem: Takes more time as the n becomes larger.
BUT FASTER THAN APPROACH 2
'''
def count0(n):
    num0 = 1
    num1 = 1
    i = 0
    while i < n:
        out = (num0 + num1)% 1000000007
        num0 = num1 % 1000000007
        num1 = out % 1000000007

        i += 1

    return num1

# ------------------------------------------------------------------------------------

n = int(input())            # 't' : no of test cases
i = 0
inputList = []          # list of test cases
while i < n:
    inputList.append(int(input()))          # taking test cases from stdin
    i += 1

# computing result for each case in the list
for ele in inputList:
    print (count0(ele))

    # Slower approach
    # print(count02(ele)% 1000000007)

    # inefficient/fails for large n
    # print(count01(ele,1)%1000000007)
