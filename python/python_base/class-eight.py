###################################################################
#
###################################################################

class Fraction:
    '''
    '''
    def __init__(self, number, denom=1):
        self.number = number
        self.denom = denom

    def __str__(self):
        return str(self.number) + '/' + str(self.denom)

    __repe__ = __str__

f = Fraction(2, 3)
print(f)

