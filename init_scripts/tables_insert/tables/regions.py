from faker import Faker
from pathlib import Path
from init_scripts.tables_insert.classes.sqlinsertconfig import SqlInsertConfig
from init_scripts.tables_insert.construct_insert_sql_request import construct_insert_sql_request
from utils.create_file import create_file
import random

fake = Faker()
Faker.seed(random.randint(1, 100000))

parameters = [{
        'region_name': fake.country(),
        'region_descript': fake.paragraph(nb_sentences=2)
    } for _ in range(20)]


sql_request_str = construct_insert_sql_request(SqlInsertConfig('regions', parameters))
create_file(
    path=str(Path(Path.cwd().parents[1], 'tables_insert_sql_scripts')),
    name='tables_insert_regions',
    ext='.sql',
    content=sql_request_str)





