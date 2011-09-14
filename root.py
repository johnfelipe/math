import cherrypy
from cherrypy.lib.static import serve_fileobj

import facts

class Root(object):
    def index(self):
        return """
<html>
    <head>
        <title>Math fact generator</title>
    </head>
    <body>
        <h1>Math fact generator</h1>
        <form action="genfacts" method="post">
            <p>Operation(s):
            <select name="op">
                <option value="+">Plus</option>
                <option value="-">Minus</option>
                <option value="">Plus and Minus</option>
            </select></p>
            <p>Minimum value: <input type="text" name="low" /></p>
            <p>Maximum value: <input type="text" name="high" /></p>
            <input type="submit" value="Generate"/>
        </form>
    </body>
</html>
"""
    index.exposed = True

    def genfacts(self, low=0, high=12, amount=30, op=''):
        fs = facts.generatefacts(int(low),int(high),int(amount),op)
        filename = 'test.txt'
        FILE = open(filename,'w')
        FILE.writelines([str(f)+'\n' for f in fs])
        FILE.close()
        RFILE = open(filename,'r')
        return serve_fileobj(RFILE,disposition='attachment',
                             content_type='.txt',name=filename)

    genfacts.exposed = True

cherrypy.quickstart(Root())
