
# Solution to Project Euler problem 1
# Copyright (c) jeamick. All rights reserved.
# 
# https://projecteuler.net/problem=1
# https://github.com/jeamick/ProjectEuler


#Maybe Better Solution 
def RefactorIterator(a, b):

    if(a%b==0):
        p = int(a/b)
    else:
        p = int(a/b) + 1

    return p
    
def SumDivInfTo1000(a):
      
    return 3 * sum(range(1, RefactorIterator(a, 3))) + 5 * sum(range(1, RefactorIterator(a, 5))) - 15 * sum(range(1, RefactorIterator(a, 15)))
        
if __name__ == "__main__":

    print(SumDivInfTo1000(1000))
