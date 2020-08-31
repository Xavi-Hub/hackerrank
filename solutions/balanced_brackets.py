#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/babead

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    deq = deque()
    
    for char in s:          # () = 1, {} = 2, [] = 3
        if char == '(':
            deq.append(1)
        elif char == '{':
            deq.append(2)
        elif char == '[':
            deq.append(3)
        elif char == ')':
            if (not deq) or deq.pop() != 1: return 'NO'
        elif char == '}':
            if (not deq) or deq.pop() != 2: return 'NO'
        elif char == ']':
            if (not deq) or deq.pop() != 3: return 'NO'

    if deq: return 'NO'
    return 'YES'