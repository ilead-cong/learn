#########################################
#
#########################################

class RoundFloat:
    '''
    '''
    def __init__(self, val):
        self.value = round(val, 2)

    def __str__(self): # str 用户；repr 解释器
        return "{0:.2f}".format(self.value)

    __repr__ = __str__

r = RoundFloat(3.1415926)
print(r)
print(type(r))
