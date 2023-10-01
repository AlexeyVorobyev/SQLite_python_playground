import sqlite3
from sqlite3 import Error
from pathlib import Path

def sql_connection():
    try:
        con = sqlite3.connect(Path(Path(__file__).parents[1], 'databases', 'economy.db'))
        return con
    except Error:
        print(Error)