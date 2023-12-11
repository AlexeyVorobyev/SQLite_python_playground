from http.server import HTTPServer, CGIHTTPRequestHandler

from flask import Flask

from modules.regions.module import RegionsModule

from threading import Thread

app = Flask('app')

class Run:
    regions_module = RegionsModule(app)

    def flask(self):
        app.run(port='3001')

    def main(self):
        server_address = ("", 3000)
        httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
        httpd.serve_forever()


run = Run()
thread = Thread(target=run.flask())
thread1 = Thread(target=run.main())
thread.start()
thread1.start()
