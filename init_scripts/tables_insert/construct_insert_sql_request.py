from utils.sql_request_to_string import sql_request_to_string
from init_scripts.tables_insert.classes.sqlinsertconfig import SqlInsertConfig


def construct_insert_sql_request(config: SqlInsertConfig) -> str:
    sql_request_string = sql_request_to_string('sql_insert_template.sql')
    sql_request_string = (sql_request_string
                          .replace('table_name', config.table_name)
                          .replace('parameters_keys', ', '.join(config.parameters[0].keys())))
    for dicts in config.parameters:
        sql_request_string += ' (' + ', '.join(['\'' + value.replace('\'', '\"') + '\'' for value in dicts.values()]) + '),\n'

    sql_request_string = ';'.join(sql_request_string.rsplit(',\n',1))
    return sql_request_string
