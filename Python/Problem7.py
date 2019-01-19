


def timer(func):
    from time import time
    def f(*args, **kwargs):
        before = time()
        rv = func(*args)
        after = time()
        print('Time elapsed: ', after - before)
        return rv
    return f
    
def isPrime(n): 
    if (n <= 1): 
        return False
    
    for i in range(2, n): 
        if (n % i == 0): 
            return False
    return True
    
@timer
def test():
    Tabu = []
    i = 0
    while(len(Tabu)<10001):
        i = i + 1
        if(isPrime(i) is True):
            Tabu.append(i)
    print i

if __name__ == '__main__':
    test()
 
