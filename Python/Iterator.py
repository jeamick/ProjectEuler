# Iterator function to mimic for loops
# All rights reserved.

class Counter:
    def __init__(self, low, high):
        # set class attributes inside the magic method __init__
        # for "initialize"
        self.current = low
        self.high = high

    def __iter__(self):
        # first magic method to make this object iterable
        return self
    
    def __next__(self):
        # second magic method
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
