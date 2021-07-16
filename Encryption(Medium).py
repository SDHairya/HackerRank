#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    count=0
    maxi=0
    for i in range(0,len(topic)-1):
        for j in range(i+1,len(topic)):
            x=int(topic[i])
            y=int(topic[j])
            z=str(x+y)
            z=z.replace("2","1")
            t=list(z)
            if maxi==t.count("1"):
                count+=1
                maxi=t.count("1")
            elif maxi<t.count("1"):
                count=1
                maxi=t.count("1")
    return maxi,count
      
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
