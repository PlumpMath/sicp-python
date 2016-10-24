def max_in_three(first, second, three):
    """
    return the max num in three args
    """
    
    f = lambda x, y: x if x>y else y
    
    return f(f(first, second), three)
    
    
#使用functools.reduce可以得到任意个参数最大值

from functools import reduce

def max_items(*args):
    """
    find max in unknown args
    """
    return reduce((lambda x, y: x if x>y else y), args)
