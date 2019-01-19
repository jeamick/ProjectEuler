# Solution to Project Euler problem 6
# Copyright (c) jeamick. All rights reserved.
# https://projecteuler.net/problem=6
# https://github.com/jeamick/ProjectEuler
  
def FunctionNcarre(n):
  '''
  Somme of n*n integers
  '''
  return (n*(n+1)*(2*n+1)/6)
  
if __name__ == '__main__':
  print FunctionNcarre(100)*FunctionNcarre(100)-FunctionNcarre(100)
