corns=[1, 5, 10, 25, 50]

def cc(amount, corns):
    """
    """
    
    if amount == 0:
        return 1
    elif amount<0 or corns.length==0:
        return 0
    else:
        return cc(amount, corns[1:]) + cc(amount-corns[0], corns)
        
        
        
        
#更优算法？？？？
