#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    sum1,sum2,sum3=sum(h1),sum(h2),sum(h3)
    while True:
        if len(h1)==0 or len(h2)==0 or len(h3)==0:
            return 0
        if sum1==sum2==sum3:
            return sum1
        if sum1>=sum2 and sum1>=sum3:
            sum1-=h1.pop(0)
        elif sum2>=sum1 and sum2>=sum3:
            sum2-=h2.pop(0)
        elif sum3>=sum1 and sum3>=sum2:
            sum3-=h3.pop(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
