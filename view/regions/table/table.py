from pathlib import Path
from models.regions.model import RegionModelBuilder
from utils.create_file import create_file


class RegionsTableView:
    def __init__(self, regions_module_arg):
        self.regions_module = regions_module_arg
        self.headers = ''
        self.values = ''
        self.styles = '''
            table, th, td {
                border:1px solid black;
            }
        '''
        self.script = open(Path(Path.cwd().parents[0], 'view', 'regions', 'table', 'table.js'), 'r').read()
        self.render()

    def __get_table_headers(self, region_dict: dict):
        headers = [key for key in region_dict.keys()]
        result_html = ''
        for header in headers:
            result_html += f'<th>{header}</th>\n'
        return result_html

    def __get_table_row(self, region_dict: dict):
        values = [key for key in region_dict.values()]
        result_html = ''
        i = 0
        for value in values:
            if i == 0:
                print('here')
                result_html += f'<td><a href="/regions/views/{value}.html">{value}</a></td>\n'
                i += 1
            else:
                result_html += f'<td>{value}</td>\n'
        return result_html

    def __get_table_rows(self, regions_dict: list[dict]):
        result_html = ''
        for region_dict in regions_dict:
            result_html += f'<tr>{self.__get_table_row(region_dict)}</tr>\n'
        return result_html

    def __construct_html(self):
        regions = self.regions_module.regions_service.get_all()
        regions_dict: list[dict] = [region.to_dict() for region in regions]

        if len(regions_dict) > 0:
            self.headers = self.__get_table_headers(regions_dict[0])
        else:
            region_dict = RegionModelBuilder().get_product().to_dict()
            self.headers = self.__get_table_headers(region_dict)

        self.values = self.__get_table_rows(regions_dict)

        pattern = f'''
            <!DOCTYPE HTML>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Таблица регионов</title>
                </head>
                <script>
                    {self.script}
                </script>
                <style>
                    {self.styles}
                </style>
                <body>
                    <h1>Таблица регионов</h1>
                    <table style='width:100%'>
                        <tr>
                            {self.headers}
                        </tr>
                        {self.values}
                    </table>
                    <button onclick="window.location=`/regions/form_add.html`;">Добавить запись</>
                </body>
            </html>
        '''
        return pattern

    def render(self):
        create_file(
            path=str(Path(Path.cwd(), 'regions')),
            name='table',
            ext='.html',
            content=self.__construct_html()
        )
