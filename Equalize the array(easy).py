#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    x=len(s)
    st=""
    root=math.sqrt(x)
    a=math.floor(root)
    b=math.ceil(root)
    row=0
    col=0
    if(a*b<x):
        row=b
        col=b
    else:
        row=a
        col=b

    for i in range(0,len(s)):

        st=st+s[i]
        for j in range(i+col,len(s),col):
            st=st+s[j]
        if(len(st)-(col-1)==x):
            break
        
        st = st + " "
    return st

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
