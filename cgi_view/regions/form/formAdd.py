from pathlib import Path
from cgi_models.regions.model import RegionModelBuilder
from cgi_utils.create_file import create_file


class RegionsFormAddView:
    def __init__(self, regions_module_arg):
        self.regions_module = regions_module_arg
        self.render()

    def __construct_html(self):
        pattern = f'''
            <!DOCTYPE HTML>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Добавление региона</title>
                </head>
                <body>
                    <h1>Добавление региона</h1>
                    <form action="/cgi-bin/regions/form_add.py">
                    <input type='text' name='region_id' style="display:none">
                        <p>id: </>
                        <input type='text' name='region_id_change'>
                        <p>Название региона: </>
                        <input type='text' name='region_name_change'>
                        <p>Описание региона: </>
                        <textarea type='text' name='region_region_descript_change' rows="10" cols="50"></textarea>
                        <button>Добавить запись</>
                    </form>
                </body>
            </html>
        '''
        return pattern

    def render(self):
        create_file(
            path=str(Path(Path.cwd(), 'regions')),
            name="form_add",
            ext='.html',
            content=self.__construct_html()
        )
