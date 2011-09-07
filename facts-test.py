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
        
        results = facts.generateFacts(low, high, amount)

        for fact in results:
            self.assertTrue(low <= fact.left)
            self.assertTrue(low <= fact.right)
            self.assertTrue(high >= fact.left)
            self.assertTrue(high >= fact.right)

    def testGenerateFactsDefaultsToZeroToTwelve(self):
        high = 12
        low = 0
        amount = 500
        
        results = facts.generateFacts(low, high, amount)

        for fact in results:
            self.assertTrue(low <= fact.left)
            self.assertTrue(low <= fact.right)
            self.assertTrue(high >= fact.left)
            self.assertTrue(high >= fact.right)

    def testGenerateFactsDefaultsThirtyFacts(self):
        high = 12
        low = 0
        
        results = facts.generateFacts(low, high)

        self.assertEquals(30,len(results))

    def testGenerateFactsCanGiveMinus(self):
        results = facts.generateFacts(op=minus)

        for fact in results:
            self.assertEquals('-',fact.sign)

    def testGenerateFactsCanGivePlus(self):
        results = facts.generateFacts(op=plus)

        for fact in results:
            self.assertEquals('+',fact.sign)

if __name__ == '__main__':
    unittest.main()

