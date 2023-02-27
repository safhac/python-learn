import http.server
import socketserver

PORT = 8001

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("host01", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()