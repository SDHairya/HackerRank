#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if (s[8]=='P' and s[:2]!="12"):
        h = int(s[0:2])
        h = h+12
        if(h==24):
            h="00"
        s = str(h)+s[2:8]
    elif(s[:2]=="12" and s[8]=='P'):
        s = s[:8]
    elif(s[:2]=="12" and s[8]=='A'):
        s = "00"+s[2:8]
    elif s[8]=='A':
        s = s[:8]
        
    return s
        
    
        
        
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
