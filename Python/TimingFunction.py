# Timing function for Euler problem using decoratoirs
# Copyright (c) jeamick. All rights reserved.
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

###############################
#########  Example ############
###############################

@timer
def test(x, y=45):
    a=[] 
    for i in range(1, 45):
        a.append(2*x+y*x-x*x)

    return x + y * 1500 + x * 45 *x 

if __name__ == "__main__":
    from time import time
    print(test(15))


##############################################
#########  Output after Execution ############
##############################################

# Time elapsed:  0.0
# 77640



