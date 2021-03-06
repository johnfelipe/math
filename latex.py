def buildlatexfile(facts):
    rectfacts = arrangerectangle(facts)
    latexfile = open('arithmetic.tex','w')
    latexfile.write(makeheader())
    latexfile.write(typesetquestions(rectfacts))
    latexfile.write(makeline())
    latexfile.write(typesetanswers(rectfacts))
    latexfile.write(makeend())
    latexfile.close()

def typesetquestions(rows):
    questions = []
    for row in rows:
        questions.append(typesetrow([typesetfact(fact) for fact in row]))
    return typesetspacedrows(questions)

def typesetanswers(rows):
    answers = ''
    for row in rows:
        answers += typesetrow([str(fact.result) for fact in row])
    return answers

def arrangerectangle(facts):
    return [ facts[r*5:r*5+5] for r in range(6) ]

def typesetfact(fact):
    if fact.sign == '+':
        op = '\opadd'    
    elif fact.sign == '-':
        op = '\opsub'
    style = '[resultstyle=\hole,carrystyle=\hole]'
    nums = '{%d}{%d}' % (fact.left, fact.right)
    return op + style + nums

def typesetrow(facts):
    hspace = r' \hspace{1in} '
    dispstart = r'\['
    dispend = r'\]' + '\n'
    dispfacts = hspace.join(facts)
    return ' '.join([dispstart,dispfacts,dispend])

def typesetspacedrows(rows):
    vspace = '\n' r'\vspace{0.75cm}' + '\n\n'
    return vspace.join(rows)

def makeheader():
    return r'''\documentclass{article}

\usepackage[hmargin=1in,vmargin=1in]{geometry}
\usepackage{xlop}

\begin{document}
\thispagestyle{empty}
\title{Arithmetic Practice}
\author{WCI}

%\maketitle
\newcommand\hole[1]{\texttt{\ }}
'''

def makeline():
    return r'''\vspace{1cm}
\begin{center}
\line(1,0){450}
\end{center}
'''

def makeend():
    return r'''
\end{document}
'''
