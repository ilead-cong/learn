#########################################
#迭代器
#########################################

class MyRange:
    '''
    '''
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
        
print("range(7):", list(range(7)))
print("myrange(7):", [i for i in MyRange(7)])