#!/usr/bin/env python3
"""
Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
Return a JSON object with the key “return_string” and a string containing every third letter from the original string

POST request in form: 
    curl -d '{"string_to_cut": "iamyourlyftdriver"}' localhost:8080

Returns: 
    {"return_string": return_string}
    where return_string is every third letter from the originql string_to_cut

Usage::
    ./server.py [<port>]
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json


class S(BaseHTTPRequestHandler):
    def _set_response(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == "/test":
            self._set_response(405)	# Method Not Allowed
            self.wfile.write("405: Method GET not avaliable for \"/test\" route. Use POST instead".encode('utf-8'))
        else: 
            self._set_response(501)	# Not Implemented
            self.wfile.write("501: Route not implemented.".encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        if self.path == "/test":
            post_data = post_data.decode('utf-8')
            message = json.loads(post_data)
            response = {"return_string": message.get('string_to_cut')[2::3]}
            response = json.dumps(response)
        
       	    self._set_response(200)		# OK
            self.wfile.write(response.encode('utf-8'))
        
        else: 
            self._set_response(501)     # Not Implemented
            self.wfile.write("501: Route not implemented.".encode('utf-8'))
        

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
