from init_utils.connection import sql_connection
from typing import List


def get_table_columns_names(table_name: str) -> List[str]:
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    res = cursor.description
    con.close()
    return list(map(lambda x: x[0], res))
