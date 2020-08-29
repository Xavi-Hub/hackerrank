#!/bin/python3

# PROBLEM:
# http://hr.gs/16xx

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    note_words = {}

    # Add all words in note to dict
    for word in note:
        if word in note_words:
            note_words[word] += 1
        else:
            note_words[word] = 1

    for word in magazine:
        if word in note_words:
            if note_words[word] != 0: note_words[word] -= 1
    
    for key in note_words:
        if note_words[key] != 0:
            print("No")
            return

    print('Yes')

magazine = ['hi', 'there', 'bob']
note = ['hi', 'there']
print(checkMagazine(magazine, note))