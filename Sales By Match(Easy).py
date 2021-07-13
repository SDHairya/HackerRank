#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    forward_turn = 0
    backward_turn = 0
    page=0
    i=0
    while (i<=n):
        page = page + 2
        if page<=p:
            forward_turn += 1
        else:
            break
        i +=1
    
    i = n+1
    page=n
    while (i>0):
        page = page - 2
        if(n%2==0 and p==n-1):
            
            backward_turn+=1
            break
        if page>=p:
            backward_turn += 1
        else:
            break
        
        i -=1
    
    return min(forward_turn,backward_turn)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
