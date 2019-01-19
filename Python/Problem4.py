# Solution to Project Euler problem 4
# Copyright (c) jeamick. All rights reserved.
# https://projecteuler.net/problem=4
# https://github.com/jeamick/ProjectEuler

def Palindrome_Number():
    palind = None
    for n in xrange(100, 1000):
        for m in xrange(100, 1000):
            prod = n * m
            if str(prod) == str(prod)[::-1]:
                if palind is None or prod > palind:
                    palind = prod
    return palind

if __name__ == "__main__":
    print(Palindrome_Number())