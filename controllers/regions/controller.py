class RegionsController:
    def __init__(self, regions_module_arg, app_arg):
        @app_arg.route('/api/regions/<id_arg>', methods=['GET'])
        def _delete(id_arg):
            print('here')
            regions_module_arg.regions_service.delete(id_arg)
            return 'True'

    # # @self.app.route('/api/regions/<id_arg>', methods=['DELETE'])
    # def delete(self):
    #     app = self.app
    #
    #     @app.route('/api/regions/<id_arg>', methods=['GET'])
    #     def _delete(self, id_arg):
    #         print(id_arg)
