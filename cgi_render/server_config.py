from http.server import HTTPServer, CGIHTTPRequestHandler
from cgi_modules.regions.module import RegionsModule

regions_module = RegionsModule()

server_address = ("", 4321)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()


