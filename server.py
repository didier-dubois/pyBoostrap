#!/usr/bin/python
#
# Didier Dubois 2016
#

import web

import view
from view import render


urls = (
    '/graph/', 'Graph',
    '/svg/(.*)', 'Svg',
    '/', 'Index',
)

class Index:
    def GET(self):
        return render.layout(view.index())

class Graph:
    def GET(self):
        return render.layout(view.graph())

class Svg:
    def GET(self, param=None):
        # No Layout for providing service
        return view.svg()


# Starting the application
if __name__ == '__main__':
    app = web.application( urls, globals())
    app.run()



