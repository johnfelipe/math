import unittest
import facts
from operations import plus,minus

class FactsTest(unittest.TestCase):

    def testMakePlus(self):
        fact = facts.makeFact(3,5,plus)

        self.assertEquals(3,fact.left)
        self.assertEquals(5,fact.right)
        self.assertEquals(8,fact.result)
        self.assertEquals('+',fact.sign)

    def testMakeMinus(self):
        fact = facts.makeFact(9,5,minus)

        self.assertEquals(9,fact.left)
        self.assertEquals(5,fact.right)
        self.assertEquals(4,fact.result)
        self.assertEquals('-',fact.sign)

    def testChoosePlusMinus(self):
        op = facts.choosePlusMinus()

        self.assertTrue(str(op) == '+' or str(op) == '-')

    def testGenerateFactsStaysWithinLimits(self):
        high = 15
        low = 2
        amount = 500
        
        results = facts.generatefacts(low, high, amount)

        for fact in results:
            self.assertTrue(low <= fact.left <= high)
            self.assertTrue(low <= fact.right <= high)

    def testGenerateFactsDefaultsToZeroToTwelve(self):
        high = 12
        low = 0
        amount = 500
        
        results = facts.generatefacts(low, high, amount)

        for fact in results:
            self.assertTrue(low <= fact.left <= high)
            self.assertTrue(low <= fact.right <= high)

    def testGenerateFactsYieldsNoNegatives(self):
        results = facts.generatefacts(amount=500, op='-')

        for fact in results:
            self.assertTrue(fact.result >= 0)

    def testGenerateFactsDefaultsThirtyFacts(self):
        high = 12
        low = 0
        
        results = facts.generatefacts(low, high)

        self.assertEquals(30,len(results))

    def testGenerateFactsCanGiveMinus(self):
        results = facts.generatefacts(op='-')

        for fact in results:
            self.assertEquals('-',fact.sign)

    def testGenerateFactsCanGivePlus(self):
        results = facts.generatefacts(op='+')

        for fact in results:
            self.assertEquals('+',fact.sign)

    def testGenerateFactsCanGiveMixOfPlusMinus(self):
        results = facts.generatefacts(amount=500)

        pluscount = 0
        minuscount = 0
        for fact in results:
            if fact.sign == '+':
                pluscount += 1
            elif fact.sign == '-':
                minuscount += 1
            else:
                self.assertFalse(True)
        self.assertEquals(500,pluscount+minuscount)
        self.assertTrue(200 < pluscount < 300)

    
if __name__ == '__main__':
    unittest.main()

