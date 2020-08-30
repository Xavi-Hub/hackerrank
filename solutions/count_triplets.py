#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/3cd5m

import math
import os
import random
import re
import sys
    
# Complete the countTriplets function below.
def countTriplets(arr, r):
    singles = {}
    doubles = {}    # keyed by second number
    triplets = {}   # keyed by third number

    for num in arr:
        if num % r == 0:
            if num/r in doubles:    # This number is the third number in a triplet, increment by number of doubles it can be appended to
                if num in triplets:
                    triplets[num] += doubles[num/r] 
                else:
                    triplets[num] = doubles[num/r]
            if num/r in singles:    # This number is the second number in a possible triplet, increment by number of singles it can be appended to
                if num in doubles:
                    doubles[num] += singles[num/r]
                else:
                    doubles[num] = singles[num/r]
        if num in singles:          # This number could be the start of a triplet
            singles[num] += 1
        else:
            singles[num] = 1


    count = 0
    for triplet_count in triplets.values():
        count += triplet_count
    return count