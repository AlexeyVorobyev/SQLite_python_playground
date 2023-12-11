import os
from pathlib import Path
from models.regions.model import RegionModel
from utils.create_file import create_file


class RegionsViewView:
    def __init__(self, regions_module_arg, region_id_arg):
        self.region_id = region_id_arg
        self.regions_module = regions_module_arg
        self.script = open(Path(Path.cwd().parents[0], 'view', 'regions', 'views', 'view.js'), 'r').read()
        self.render()

    def __construct_html(self):
        region: RegionModel = self.regions_module.regions_service.get_by_id(self.region_id)

        pattern = f'''
            <!DOCTYPE HTML>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Просмотр региона</title>
                </head>
                <body>
                    <h1>Просмотр региона</h1>
                    <p>id: {region.id}</p>
                    <p>Название: {region.region_name}</p>
                    <p>Описание: {region.region_descript}</p>
                    <button onclick="window.location=`/regions/forms_edit/{region.id}.html`;">Изменить запись</button>
                    <form id='form'>
                        <input type='text' name='region_id' value={str(region.id)} id='input_region_id' style="display:none">
                        <button>Удалить запись</button>
                    </form>
                </body>
                <script>
                    {self.script}
                </script>
            </html>
        '''
        return pattern

    def render(self):
        create_file(
            path=str(Path(Path.cwd(), 'regions', 'views')),
            name=str(self.region_id),
            ext='.html',
            content=self.__construct_html()
        )

    def delete(self):
        os.remove(str(Path(Path.cwd(), 'regions', 'views', f"{str(self.region_id)}.html")))


class RegionsViewsView:
    def __init__(self, regions_module_arg):
        self.regions_module = regions_module_arg
        self.regions_view_view_collection: list[RegionsViewView] = self.__get_regions_view_view_collection()
        self.render()

    def __get_regions_view_view_collection(self):
        regions: list[RegionModel] = self.regions_module.regions_service.get_all()
        return [RegionsViewView(self.regions_module, region.id) for region in regions]

    def render(self):
        for region_view_view in self.regions_view_view_collection:
            region_view_view.render()
