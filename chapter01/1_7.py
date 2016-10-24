"""
f(n)=f(n-1)+2f(n-2)+3f(n-3)
当n<3, f(n)=n

f(0)=0, f(1)=1, f(2)=2

f(3)=f(2)+2f(1)+3f(0)

"""

def f(n):
    """
    """
    
    a=0
    b=1
    c=2
    k=3
    
    while k<=n:
        temp = c+2*b+3*a
        a = b
        b = c
        c = temp
        k += 1
    return c
