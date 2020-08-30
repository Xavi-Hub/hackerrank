#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/3apgt

import math
import os
import random
import re
import sys

def swap(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            swap(arr, i, arr[i] - 1)
            count += 1
    return count