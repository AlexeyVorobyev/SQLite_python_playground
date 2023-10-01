from utils.path_to_file import path_to_file


def sql_request_to_string(sql_file_name: str) -> str:
    with open(path_to_file(sql_file_name), 'r') as sql_file:
        return sql_file.read()
