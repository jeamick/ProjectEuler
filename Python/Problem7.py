# Solution to Project Euler problem 7
# Copyright (c) jeamick. All rights reserved.
# https://projecteuler.net/problem=7
# https://github.com/jeamick/ProjectEuler

def timer(func):
    '''
    Timing Function using decorator
    '''
    from time import time
    def f(*args, **kwargs):
        before = time()
        rv = func(*args)
        after = time()
        print('Time elapsed: ', after - before)
        return rv
    return f
        
 def fast_nth_prime(n :int , limit=125000 :int):
    
    if limit % 2 != 0: 
        limit += 1
    primes = [True] * limit
    primes[0], primes[1] = [None] * 2
    count = 0 # how many primes have we found?
    for ind, val in enumerate(primes):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes[ind*2::ind] = [False] * (((limit - 1)//ind) - 1)
            count += 1
        if count == n: 
            return ind
    return False

@timer
def test():
    print(fast_nth_prime(10001))

if __name__ == '__main__':
    test()
 
