def typesetfact(fact):
    if fact.sign == '+':
        op = '\opadd'    
    style = '[resultstyle=\hole,carrystyle=\hole]'
    nums = '{%d}{%d}' % (fact.left, fact.right)
    return op + style + nums