#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/16xx

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    if d == len(a):
        return a

    b = a.copy()

    for i in range(len(a)):
        new_pos = (i - d) % len(a)
        b[new_pos] = a[i]

    return b