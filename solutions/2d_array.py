#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/abbdcb

import math
import os
import random
import re
import sys

# Returns the hourglass sum using (x_pos, y_pos) as center
def compute_hourglass(arr, y_pos, x_pos):
    sum = 0
    for i in range(3):      # Sum top and bottom rows
        sum += arr[y_pos-1][x_pos-1 + i]
        sum += arr[y_pos+1][x_pos-1 + i]
    sum += arr[y_pos][x_pos]
    return sum


# Complete the hourglassSum function below.
def hourglassSum(arr):      # 6x6
    max_sum = -100           # -9 is lowest number, -9 * 7 = -63 as lowest possibility
    for i in range(1,5):
        for j in range(1,5):
            max_sum = max(max_sum, compute_hourglass(arr, i, j))
    return(max_sum)