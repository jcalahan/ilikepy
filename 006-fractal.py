# This module defines a mandelbrot function exposed via an HTTP service.

# To use it:
#  a) run 'python fractal.py'
#  b) point your web browser to http://localhost:8000

from urlparse import urlparse, parse_qs
import SimpleHTTPServer
import SocketServer

port = 8000

def mandelbrot(f, width=500, height=400, max_count=20): 
    '''
      Basic Mandelbrot Algorithm lifted from
       http://codereview.stackexchange.com/questions/107316/mandelbrot-set-fractal
    '''

    f.write('''<html>
<head>
<title>Mandelbrot (%(width)s x %(height)s)</title>
<style>
svg { background-color: beige; }
rect { fill: rgb(0,0,255); stroke-width: 1; }
</style>
</head>
<body>
<h2> The Mandelbrot set a particular set of complex numbers that has a highly
convoluted fractal boundary when plotted. </h2>
<svg width='%(width)s' height='%(height)s'>
<text x='5' y='15' fill='red'>Max Count = %(count)s</text>
''' % {'width':width, 'height':height, 'count':max_count})

    for row in range(height):
        for col in range(width):
            c = complex(
                (col - float(width)/2.0)*5.0/float(width),
                (row - float(height)/2.0)*5.0/float(height)
            )
            iteration = 0
            z = 0
            while abs(z) < 2 and iteration < max_count:
                z = z**2 + c
                iteration += 1
            if abs(z) < 2:
                f.write("<rect x='%s' y='%s' width='1' height='1'/>\n" % (col, row))

    f.write("</body></svg></html>\n")

#f = open("foo.html", "w")
#mandelbrot(f)
#f.close()

def pickParam(params, name, default):
    if name in params:
        values = params[name]
        if len(values) > 0:
            return int(values[0])
    return default

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        width = pickParam(params, 'w', 500)
        height = pickParam(params, 'h', 400)
        max_count = pickParam(params, 'c', 20)
        mandelbrot(self.wfile, width, height, max_count)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', port), Handler)

print 'serving at', port
server.serve_forever()
