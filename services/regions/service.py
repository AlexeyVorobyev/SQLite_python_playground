from models.regions.model import RegionModel
from repositories.regions.repository import RegionRepository


class RegionsService:
    def __init__(self, regions_module_arg):
        self.regions_module = regions_module_arg
        self.repository = RegionRepository()

    def get_all(self):
        return self.repository.get_all()

    def delete(self, id_arg):
        view_collection = self.regions_module.regions_views_view.regions_view_view_collection
        filtered = filter(lambda item: str(item.region_id) == str(id_arg), view_collection)
        list_filtered = list(filtered)
        list_filtered[0].delete()
        self.repository.delete_by_id(id_arg)
        self.regions_module.regions_table_view.render()

    def get_by_id(self, id_arg):
        return self.repository.get_by_id(id_arg)

    def post(self, region_model_instance: RegionModel):
        self.repository.post(region_model_instance)
