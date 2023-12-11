from utils.sql_gen_select_all_query_based_on_model import sql_gen_select_all_query_based_on_model
from utils.sql_gen_delete_by_id_query_based_on_model import sql_gen_delete_by_id_query_based_on_model
from utils.sql_gen_insert_based_on_model import sql_gen_insert_based_on_model
from models.regions.model import RegionModel
from models.regions.model import RegionModelBuilder
from utils.sql_execute import sql_execute
from init_utils.connection import sql_connection
from pprint import pprint


class RegionRepositorySQL:
    def __init__(self):
        self.con = sql_connection()
        self.get_all_sql = sql_gen_select_all_query_based_on_model(RegionModel)
        self.delete_by_id_sql = sql_gen_delete_by_id_query_based_on_model(RegionModel)
        self.post = sql_gen_insert_based_on_model(RegionModel)


class RegionRepository:
    collection: list[RegionModel] = []

    def __init__(self):
        self.sql_queries = RegionRepositorySQL()
        self.__update_repository()

    def __update_repository(self):
        result = sql_execute(self.sql_queries.con, self.sql_queries.get_all_sql, True)

        new_collection = []
        for item in result:
            region = (RegionModelBuilder()
                      .set_id(item[0])
                      .set_region_name(item[1])
                      .set_region_descript(item[2])
                      .get_product())
            new_collection.append(region)
        self.collection = new_collection

    def get_all(self):
        return self.collection

    def delete_by_id(self, id_arg: int):
        sql_execute(self.sql_queries.con, self.sql_queries.delete_by_id_sql(id_arg))
        self.__update_repository()

    def post(self, region: RegionModel):
        sql_execute(self.sql_queries.con, self.sql_queries.post(region))
        self.__update_repository()

    def get_by_id(self, id_arg: int):
        for item in self.collection:
            if item.id == id_arg:
                return item
        return 'item with this id not found'
