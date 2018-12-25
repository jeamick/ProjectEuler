# Solution to Project Euler problem 2
# Copyright (c) jeamick. All rights reserved.
# https://projecteuler.net/problem=2
# https://github.com/jeamick/ProjectEuler


# Maybe Better/Efficient Solution 
def fib_lim(limit):
    
    a, b = 0, 1
    while a < limit:
        if not a % 2:         
            yield a
        a, b = b, a + b

if __name__ == "__main__":
    print(sum(fib_lim(4000000)))