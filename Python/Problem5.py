# Solution to Project Euler problem 5
# Copyright (c) jeamick. All rights reserved.
# https://projecteuler.net/problem=5
# https://github.com/jeamick/ProjectEuler

def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) / gcd(a, b)
  
if __name__ == '__main__':
  
  llcm = lcm(11, 12)
  for n in range(12, 20):
    llcm = lcm(n, llcm)
  print llcm
 
