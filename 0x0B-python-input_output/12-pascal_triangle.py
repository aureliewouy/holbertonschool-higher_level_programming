#!/usr/bin/python3
"""
Pascal's Triangle
"""
def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)

    return res

def pascal_triangle(n):
    """
    Returns a list of lists of integer representing the Pascal's triangle
    """
    l = []
    if n <= 0:
        return l
    
