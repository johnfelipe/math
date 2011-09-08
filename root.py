import cherrypy
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
            <input type="submit" value="Generate"/>
        </form>
    </body>
</html>
"""
    index.exposed = True

    def genfacts(self):
        fs = facts.generateFacts()
        return str(fs)
    genfacts.exposed = True

cherrypy.quickstart(Root())
