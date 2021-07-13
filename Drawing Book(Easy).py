#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count=0
    valley_count=0
    for i in range(0,len(path)):
        
        if(count==0 and path[i]=='D'):
            for j in range(i,len(path)):
                if(path[j]=='U'):
                    count+=1
                elif(path[j]=='D'):
                    count-=1
                if(count==0):
                    valley_count+=1 
                    break   
        if(path[i]=='U'):
            count+=1
        elif(path[i]=='D'):
            count-=1
            
    return valley_count
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
