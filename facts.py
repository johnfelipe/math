from collections import namedtuple
from random import choice
from operations import plsmns

Fact = namedtuple('Fact','left,right,result,op')

def makeFact(left,right,op):
    result = op.do(left,right)
    return Fact(left,right,result,op)

def choosePlusMinus():
    return choice(plsmns)   
