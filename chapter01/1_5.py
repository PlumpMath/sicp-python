def x():
    return x()
    
def test(x, y):
    if x == 0:
        return x
    return y
    
a = 0
test(a, x())
