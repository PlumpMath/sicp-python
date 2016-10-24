#!-*- coding: utf8 -*-
from math import sqrt

def divisor(n):
    for x in range(2, int(sqrt(n))+1):
        if not n%x:
            return x
