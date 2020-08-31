#!/bin/python3
# 
# COMPLETED
# 
# PROBLEM:
# http://hr.gs/16xx

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return(str(self.name) + " " + str(self.score))
        
    # pylint: disable=E0213
    def comparator(a, b):
        if a.score == b.score:
            if a.name == b.name:
                return 0
            return(-1 if a.name < b.name else 1)
        return(-1 if a.score > b.score else 1)
        
n = int(input())