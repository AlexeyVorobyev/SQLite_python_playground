class RegionModelBuilder:
    def __init__(self):
        self.product = RegionModel()

    def set_id(self, id_arg):
        self.product.id = id_arg
        return self

    def set_region_name(self, region_name_arg):
        self.product.region_name = region_name_arg
        return self

    def set_region_descript(self, id_region_descript):
        self.product.region_descript = id_region_descript
        return self

    def get_product(self):
        return self.product


class RegionModel:
    database_table_name = 'regions'

    def __init__(self):
        self.id = None
        self.region_name = None
        self.region_descript = None

    def __str__(self):
        return (f'database_table_name: {self.database_table_name}; '
                f'id: {self.id}; '
                f'region_name: {self.region_descript}; '
                f'region_descript: {self.region_descript}')

    def to_dict(self):
        return {
            'id': self.id,
            'region_name': self.region_name,
            'region_descript': self.region_descript
        }
