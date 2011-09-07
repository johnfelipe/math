from collections import namedtuple
from random import choice, randint
from operations import plsmns,plus,minus

Fact = namedtuple('Fact','left,right,result,sign')

def makeFact(left,right,op):
    result = op.do(left,right)
    return Fact(left,right,result,str(op))

def choosePlusMinus():
    return choice(plsmns)   

def generateFacts(low=0, high=12, amount=30, op=plus):
    return [generateFact(low,high,op) for _ in range(amount) ]

def generateFact(low,high,op):
    left = randint(low,high)
    right = randint(low,high)
    return makeFact(left,right,op)
