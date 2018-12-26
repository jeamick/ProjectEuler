# Timing function for Euler problem using decoratoirs
# Credit to James Powell talk about 'So you want to be a Python expert'. All rights reserved.
# https://projecteuler.net/problem=3
# https://github.com/jeamick/ProjectEuler

def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args)
        after = time()
        print('Time elapsed: ', after - before)
        return rv
    return f

def ntimes(f):
    def wrapper(*args, **kwargs):
        for _ in range(n):
            rv = f(*args, **kwargs)
        return rv
    return wrapper
###############################
#########  Example ############
###############################

@ntimes
def test(x, y=45):
    return [2*x+y*x-x*x for i in range(x*y)][45]

if __name__ == "__main__":
    n = 2 
    from time import time
    print(test(15))


##############################################
#########  Output after Execution ############
##############################################

# Time elapsed:  0.0
# 480



