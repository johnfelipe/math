class Operation(object):
    def __init__(self,sign):
        self.sign = sign
        if sign == '+':
            self.op = lambda x,y: x+y
        elif sign == '-':
            self.op = lambda x,y: x-y

    def do(self, left, right):
        return self.op(left,right)

    def __repr__(self):
        return self.sign

    __str__ = __repr__

plus = Operation('+')
minus = Operation('-')
plsmns = [plus,minus]
