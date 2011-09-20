import unittest

import latex
from facts import Fact

class LatexTest(unittest.TestCase):

    def testArrangeRectangle(self):
        thirty = range(30)
        
        latex rect = arrangerectangle(thirty)

        self.assertEquals([0,1,2,3,4],rect[0])
        for row in range(6):
            start = row*5
            self.assertEquals(range(start,start+5),rect[row])

    def testMakeSum(self):
        addfact = Fact(123,45,168,'+')
        expected = '\opadd[resultstyle=\hole,carrystyle=\hole]{123}{45}'

        texfact = latex.typesetfact(addfact)

        self.assertEquals(expected,texfact)

    def testMakeDiff(self):
        subfact = Fact(123,45,78,'-')
        expected = '\opsub[resultstyle=\hole,carrystyle=\hole]{123}{45}'

        texfact = latex.typesetfact(subfact)

        self.assertEquals(expected,texfact)
    
    def testMakeRow(self):
        row = [ 'one', 'two', 'three' ]
        expected = r'''\[ one \hspace{1in} two \hspace{1in} three \]
'''
    
    def testMakeSpacedRows(self):
        rows = [ 'one\n', 'two\n', 'three\n' ]
        expected = r'''one

\vspace{0.75cm}

two

\vspace{0.75cm}

three
'''

        texrows = latex.typesetspacedrows(rows)

        self.assertEquals(expected,texrows)

    def testMakeHeader(self):
        expected = r'''\documentclass{article}

\usepackage[hmargin=1in,vmargin=1in]{geometry}
\usepackage{xlop}

\begin{document}
\thispagestyle{empty}
\title{Arithmetic Practice}
\author{WCI}

%\maketitle
\newcommand\hole[1]{\texttt{\ }}
'''

        header = latex.makeheader()

        self.assertEquals(expected, header)

    def testMakeLine(self):
        expected = r'''\vspace{1cm}
\begin{center}
\line(1,0){450}
\end{center}
'''

        line = latex.makeline()

        self.assertEquals(expected, line)

    def testMakeEnd(self):
        expected = r'''
\end{document}
'''

        end = latex.makeend()

        self.assertEquals(expected, end)

if __name__ == '__main__':
    unittest.main()

