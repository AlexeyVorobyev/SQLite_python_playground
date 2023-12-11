import cgi
import html
from render.server_config import regions_module

form = cgi.FieldStorage()
region_id = html.escape(form.getfirst("region_id", None))
regions_module.regions_service.delete(region_id)

pattern = '''
    <!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Удаление записи</title>
            </head>
            <body>
                <h1>Запись удалена!</>
                <button onclick="window.location=`/regions/table.html`;">Вернуться к таблице</>
            </body>
        </html>
        '''
print("Content-type: text/html\n")
print(pattern)
