from utils.connection import sql_connection
from typing import List


def get_tables_names() -> List[str]:
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    res = cursor.fetchall()
    con.close()
    return list(map(lambda x: x[0], res))
