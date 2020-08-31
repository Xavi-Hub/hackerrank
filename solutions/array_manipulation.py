#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/deabde

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    for query in queries:
        start = query[0] - 1
        end = query[1] - 1
        addend = query[2]

        arr[start] += addend
        if end + 1 < n:
            arr[end+1] -= addend
    
    current_addend = 0
    current_max = 0
    for i in range(n):
        current_addend += arr[i]
        current_max = max(current_max, current_addend)
    return current_max