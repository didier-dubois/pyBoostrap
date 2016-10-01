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

menus=( ('Home', '/'),
        ('Graph', '/graph/')
        )

def css(ids, key):
    if ids == key: return 'active'
    return ''

def menu(key):
    return [ (row[0], row[1], css(row[0], key) ) for row in menus ]


class Index:
    def GET(self):
        return render.layout(view.index(), menu('Home'))

class Graph:
    def GET(self):
        return render.layout(view.graph(), menu('Graph'))

class Svg:
    def GET(self, param=None):
        # No Layout for providing service
        return view.svg()


# Starting the application
if __name__ == '__main__':
    app = web.application( urls, globals())
    app.run()



