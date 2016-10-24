def exp(b, n):
    """
    """
    
    a = 1
    while n>1:
        if n%2:
            a *= b
        n /= 2
        b **= 2
    a *= b
    return a
