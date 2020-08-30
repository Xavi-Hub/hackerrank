#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/ec3

import math
import os
import random
import re
import sys

anagrams = {}

def n_choose_two(n):
    return n * (n - 1) / 2

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    global anagrams
    anagrams = {}

    # Iterate through all substrings, updating count of sorted substring
    for length in range(1, len(s)): # Length of anagrams we're looking for
        for pos in range(len(s) - length + 1):    # Position of possible anagram start
            substring = s[pos:pos+length]
            sorted_sub = ''.join(sorted(substring))
            if sorted_sub in anagrams:
                anagrams[sorted_sub] += 1
            else:
                anagrams[sorted_sub] = 1
    
    total = 0
    for count in anagrams.values():
        total += n_choose_two(count)
    return int(total)
