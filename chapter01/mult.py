#! -*- coding: utf8 -*-

"""
俄罗斯农民乘法
"""

def multiple(a , b):
    c = []
    while a>1:
        if a%2:
            c.append(b)
        a /= 2
        b *= 2
    for x in c:
        b += x
    return b
