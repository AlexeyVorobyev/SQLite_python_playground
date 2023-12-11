from services.regions.service import RegionsService
from controllers.regions.controller import RegionsController


class RegionsModule:
    def __init__(self,app_arg):
        self.regions_service = RegionsService(self)
        self.regions_controller = RegionsController(self,app_arg)
