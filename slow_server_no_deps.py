import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

import time


class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        time.sleep(200)

if __name__ == '__main__':
    BaseHTTPServer.test(MyRequestHandler, BaseHTTPServer.HTTPServer)
