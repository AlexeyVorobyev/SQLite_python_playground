import random
from pathlib import Path
from utils.get_tables_names import get_tables_names
from utils.get_table_columns_names import get_table_columns_names
from utils.create_file import create_file


def construct_select_sql_request(table: str,column:str ) -> str:
    return f'SELECT {column} FROM {table}'


tables_names = get_tables_names()
for i in range(20):
    rand_table_int = random.randint(0, len(tables_names) - 1)
    table_columns_names = get_table_columns_names(tables_names[rand_table_int])
    rand_column_int = random.randint(0, len(table_columns_names) - 1)

    create_file(
        path=str(Path(Path.cwd(), 'sql_scripts')),
        name=f'select_{table_columns_names[rand_column_int]}_{tables_names[rand_table_int]}',
        ext='.sql',
        content=construct_select_sql_request(tables_names[rand_table_int], table_columns_names[rand_column_int]))
