import unittest
import facts
from operations import plus,minus

class FactsTest(unittest.TestCase):

    def testMakePlus(self):
        fact = facts.makeFact(3,5,plus)

        self.assertEquals(3,fact.left)
        self.assertEquals(5,fact.right)
        self.assertEquals(8,fact.result)
        self.assertEquals('+',str(fact.op))

    def testMakeMinus(self):
        fact = facts.makeFact(9,5,minus)

        self.assertEquals(9,fact.left)
        self.assertEquals(5,fact.right)
        self.assertEquals(4,fact.result)
        self.assertEquals('-',str(fact.op))

    def testChoosePlusMinus(self):
        op = facts.choosePlusMinus()

        self.assertTrue(str(op) == '+' or str(op) == '-')

if __name__ == '__main__':
    unittest.main()

