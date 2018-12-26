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
    return [2*x+y*x-x*x for i in range(x*y)][45]

if __name__ == "__main__":
    from time import time
    print(test(15))


##############################################
#########  Output after Execution ############
##############################################

# Time elapsed:  0.0
# 480



