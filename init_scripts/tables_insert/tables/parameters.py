from faker import Faker
from pathlib import Path
from init_scripts.tables_insert.classes.sqlinsertconfig import SqlInsertConfig
from init_scripts.tables_insert.construct_insert_sql_request import construct_insert_sql_request
from utils.create_file import create_file
import random

fake = Faker()
Faker.seed(random.randint(1, 100000))

parameters = [{
        'parameter_name': fake.word(),
        'measure_id': str(random.randint(1, 20))
    } for _ in range(20)]


sql_request_str = construct_insert_sql_request(SqlInsertConfig('parameters', parameters))
create_file(
    path=str(Path(Path.cwd().parents[1], 'tables_insert_sql_scripts')),
    name='tables_insert_parameters',
    ext='.sql',
    content=sql_request_str)





