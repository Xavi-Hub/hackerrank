#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/3hmvs

import math
import os
import random
import re
import sys

num_freqs = {}      # num_freqs[key] is the frequency of "key" in the database 
freqs_count = {}    # There are freqs_count[key] amount of numbers with frequency "key" in the database
outputs = []

def safe_increment(k, d):
    if k in d:
        d[k] += 1
    else:
        d[k] = 1

def safe_decrement(k, d):
    if k in d:
        d[k] -= 1
        if d[k] < 0: d[k] = 0
    else:
        d[k] = 0

def process_query(query):
    global num_freqs, freqs_count, outputs
    query_type = query[0]
    query_val = query[1]

    if query_type == 1:   # Add to database
        safe_increment(query_val, num_freqs)
        safe_increment(num_freqs[query_val], freqs_count)
        safe_decrement(num_freqs[query_val]-1, freqs_count)

    elif query_type == 2: # Remove from database
        if query_val in num_freqs and num_freqs[query_val] != 0:
            safe_decrement(query_val, num_freqs)
            safe_increment(num_freqs[query_val], freqs_count)
            safe_decrement(num_freqs[query_val]+1, freqs_count)

    else:               # Add to output
        if query_val in freqs_count and freqs_count[query_val] > 0:
            outputs.append(1)
        else:
            outputs.append(0)



# Complete the freqQuery function below.
def freqQuery(queries):

    for query in queries:
        process_query(query)

    return(outputs)