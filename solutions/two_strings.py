#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/fnu

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    chars = {}
    for char in s1:
        chars[char] = 1

    for char in s2:
        if char in chars: return('YES')
    return('NO')