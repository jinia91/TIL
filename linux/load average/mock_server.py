#!/usr/bin/python

import BaseHTTPServer

class MyRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'success')

def run(server_class=BaseHTTPServer.HTTPServer, handler_class=MyRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print('Starting simple_http_server on http://localhost:8080')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
