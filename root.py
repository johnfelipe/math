from subprocess import call

import cherrypy
from cherrypy.lib.static import serve_fileobj

import facts
import latex

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
        latex.buildlatexfile(fs)
        filename = 'arithmetic.pdf'
        call('pdflatex arithmetic.tex', shell=True)
        returnfile = open(filename,'rb')
        return serve_fileobj(returnfile,disposition='attachment',
                             content_type='application/pdf',name=filename)

    genfacts.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8008})
cherrypy.quickstart(Root())
