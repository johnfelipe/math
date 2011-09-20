import unittest

import latex
from facts import Fact

class LatexTest(unittest.TestCase):

    def testMakeSum(self):
        addfact = Fact(123,45,168,'+')
        expected = '\opadd[resultstyle=\hole,carrystyle=\hole]{123}{45}'

        texfact = latex.typesetfact(addfact)

        self.assertEquals(expected,texfact)

if __name__ == '__main__':
    unittest.main()

