from pathlib import Path
from init_utils.connection import sql_connection


def sql_tables(con, sql_file_name: str, prefix: str):
    cursor_obj = con.cursor()
    with open(Path(Path.cwd(), f'{prefix}/{sql_file_name}'), 'r') as sql_file:
        sql_request = sql_file.read()
        cursor_obj.execute(sql_request)
        con.commit()


sql_files_names = [
    'tables_creation_sectors.sql',
    'tables_creation_regions.sql',
    'tables_creation_measures.sql',
    'tables_creation_parameters.sql',
    'tables_creation_fact_parameters.sql'
]

con = sql_connection()

for sql_file_name in sql_files_names:
    sql_tables(con, sql_file_name,'tables_creation_sql_scripts')

sql_files_names_2 = [
    'tables_insert_sectors.sql',
    'tables_insert_regions.sql',
    'tables_insert_measures.sql',
    'tables_insert_parameters.sql',
    'tables_insert_fact_parameters.sql'
]

for sql_file_name in sql_files_names_2:
    sql_tables(con, sql_file_name,'tables_insert_sql_scripts')
