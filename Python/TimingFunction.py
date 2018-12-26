# Timing function for Euler problem using decorators
# Credit to James Powell talk about 'So you want to be a Python expert'. All rights reserved.

def timer(func):
    from time import time
    def f(*args, **kwargs):
        before = time()
        rv = func(*args)
        after = time()
        print('Time elapsed: ', after - before)
        return rv
    return f

def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print(('Run {} : {.__name__} '.format(_, f)))
                rv = f(*args, **kwargs)
            return rv
        return wrapper
    return inner

###############################
#########  Example ############
###############################

@ntimes(2)
@timer
def test(x, y=45):
    return [2*x+y*x-x*x for i in range(x*y)][45]


if __name__ == "__main__":
    print(test(15))

##############################################
#########  Output after Execution ############
##############################################

# Run 0 : f
# Time elapsed:  0.0
# Run 1 : f
# Time elapsed:  0.0
# 480