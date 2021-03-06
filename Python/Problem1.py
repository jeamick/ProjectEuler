# Solution to Project Euler problem 1
# Copyright (c) jeamick. All rights reserved.
# https://projecteuler.net/problem=1
# https://github.com/jeamick/ProjectEuler


# Maybe Better/Efficient Solution 
def RefactorIterator(a :int, b: int):
    return int(a/b) if (a%b==0) else int(a/b) + 1
    
def SumDivInfToNmbre(Nmbre :int): 
    return 3 * sum(range(1, RefactorIterator(Nmbre, 3))) + 5 * sum(range(1, RefactorIterator(Nmbre, 5))) - 15 * sum(range(1, RefactorIterator(Nmbre, 15)))
        
if __name__ == "__main__":
    print(SumDivInfToNmbre(1000))
