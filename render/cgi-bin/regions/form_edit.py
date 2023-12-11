import cgi
import html

form = cgi.FieldStorage()
region_id = html.escape(form.getfirst("region_id", None))

pattern = '''
    <!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка </title>
            </head>
            <body>
                <button onclick="window.location=`/regions/table.html`;">Вернуться к таблице</>
            </body>
        </html>
        '''
print("Content-type: text/html\n")
print(pattern)