# Solution to Project Euler problem 3
# Copyright (c) jeamick. All rights reserved.
# https://projecteuler.net/problem=3
# https://github.com/jeamick/ProjectEuler

def primeFactors(n :int): 
    ListOfPrimeFactor = [] 
    while n % 2 == 0: 
        ListOfPrimeFactor.append(2), 
        n = n / 2
          
    for i in range(3, int(math.sqrt(n))+1, 2):   
        while n % i == 0: 
            ListOfPrimeFactor.append(int(i)), 
            n = n / i 
              
    if n > 2: 
        ListOfPrimeFactor.append(int(n))
    
    return ListOfPrimeFactor

if __name__ == "__main__":
    import math
    print(primeFactors(600851475143)[len(primeFactors(454822))-1])
