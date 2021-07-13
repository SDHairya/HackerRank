#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    m=min(b)
    ma=max(a)
    count=0
    for x in range(ma,m+1):
        l=[]
        l1=[]

        for i in range(0,len(a)):
            if(x%a[i]==0):
                l.append(1)
            else:
                l.append(0)
                
        for i in range(0,len(b)):
            if(b[i]%x==0):
                l1.append(1)
            else:
                l1.append(0)
                
        count+=all(l)*all(l1)
                  
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
