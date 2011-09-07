from collections import namedtuple
from random import choice
from random import randint
from operations import plsmns
from operations import plus
from operations import minus

Fact = namedtuple('Fact','left,right,result,sign')

def makeFact(left,right,op):
    result = op.do(left,right)
    return Fact(left,right,result,str(op))

def choosePlusMinus():
    return choice(plsmns)   

def generateFacts(low=0, high=12, amount=30, op=None):
    return [generateFact(low,high,op) for _ in range(amount) ]

def generateFact(low,high,op):
    left = randint(low,high)
    right = randint(low,high)
    opchoice = op if op else choosePlusMinus()
    if str(opchoice) == '-' and right > left:
        left, right = right, left
    return makeFact(left,right,opchoice)
