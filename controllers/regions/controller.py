from services.regions.service import RegionsService


class RegionsController:
    def __init__(self, regions_module_arg, app_arg):
        self.app = app_arg
        self.regions_service: RegionsService = regions_module_arg.regions_service

        @self.app.route('/api/regions/<id_arg>', methods=['DELETE'])
        def delete(id_arg):
            self.regions_service.delete(id_arg)
            return 'True'

        @self.app.route('/api/regions/<id_arg>', methods=['GET'])
        def get_by_id(id_arg):
            return self.regions_service.get_by_id(id_arg).to_dict()

        @self.app.route('/api/regions/', methods=['GET'])
        def get_all():
            return [region.to_dict() for region in self.regions_service.get_all()]
