#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    ans = []
    
    for i in range (0,len(arr)):
        Sum=0
        for j in range (0,len(arr)):
            if (j == i):
                continue
            else:
                Sum = Sum + arr[j]
        ans.append(Sum)
        
    print(min(ans),max(ans))
                

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
