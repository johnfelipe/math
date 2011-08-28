import unittest
import operations

class OperationsTest(unittest.TestCase):

    def testAddStringIsPlus(self):
        add = operations.Operation('+')

        self.assertEquals('+',str(add))

    def testAddAdds(self):
        add = operations.Operation('+')

        self.assertEquals(7, add.do(3,4))

    def testSubtractStringIsMinus(self):
        subtract = operations.Operation('-')

        self.assertEquals('-',str(subtract))

    def testAddAdds(self):
        subtract = operations.Operation('-')

        self.assertEquals(3, subtract.do(8,5))

    def testPlusIsDefined(self):
        p = operations.plus

        self.assertEquals('+',str(p))
        self.assertEquals(7, p.do(3,4))

    def testMinusIsDefined(self):
        m = operations.minus

        self.assertEquals('-',str(m))
        self.assertEquals(3, m.do(7,4))

if __name__ == '__main__':
    unittest.main()
