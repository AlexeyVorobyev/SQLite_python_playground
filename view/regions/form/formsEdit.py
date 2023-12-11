from pathlib import Path
from models.regions.model import RegionModelBuilder, RegionModel
from utils.create_file import create_file


class RegionsFormEditView:
    def __init__(self, regions_module_arg, region_id_arg):
        self.regions_module = regions_module_arg
        self.region_id = region_id_arg
        self.render()

    def __construct_html(self):
        region: RegionModel = self.regions_module.regions_service.get_by_id(self.region_id)

        pattern = f'''
            <!DOCTYPE HTML>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Изменение региона</title>
                </head>
                <body>
                    <h1>Изменение региона</h1>
                    <form action="/cgi-bin/regions/form_edit.py">
                        <input type='text' name='region_id' value={str(self.region_id)} style="display:none">
                        <p>id: </>
                        <input type='text' name='region_id_change' value={str(region.id)}>
                        <p>Название региона: </>
                        <input type='text' name='region_name_change' value={str(region.region_name)}>
                        <p>Описание региона: </>
                        <textarea type='text' name='region_region_descript_change' rows="10" cols="50">{str(region.region_descript)}</textarea>
                        <button >Изменить запись</>
                    </form>
                </body>
            </html>
        '''
        return pattern

    def render(self):
        create_file(
            path=str(Path(Path.cwd(), 'regions','forms_edit')),
            name="",
            ext=f'{self.region_id}.html',
            content=self.__construct_html()
        )


class RegionsFormsEditView:
    def __init__(self, regions_module_arg):
        self.regions_module = regions_module_arg
        self.regions_view_view_collection: list[RegionsFormEditView] = self.__get_regions_view_view_collection()
        self.render()

    def __get_regions_view_view_collection(self):
        regions: list[RegionModel] = self.regions_module.regions_service.get_all()
        return [RegionsFormEditView(self.regions_module, region.id) for region in regions]

    def render(self):
        for region_view_view in self.regions_view_view_collection:
            region_view_view.render()
