from flask import Flask
from modules.regions.module import RegionsModule


class Modules:
    app = Flask('app')
    regions_module = RegionsModule(app)

    @staticmethod
    def run_server():
        Modules.app.run(port=4321)
