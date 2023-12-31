from cgi_models.regions.model import RegionModel
from cgi_repositories.regions.repository import RegionRepository


class RegionsService:
    def __init__(self):
        self.repository = RegionRepository()

    def get_all(self):
        return self.repository.get_all()

    def delete(self, id_arg):
        self.repository.delete_by_id(id_arg)

    def get_by_id(self, id_arg):
        return self.repository.get_by_id(id_arg)

    def post(self, region_model_instance: RegionModel):
        self.repository.post(region_model_instance)
