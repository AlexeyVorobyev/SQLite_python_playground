from typing import Dict, List


class SqlInsertConfig:
    table_name: str
    parameters: List[Dict[str, str]]

    def __init__(self, table_name, parameters):
        self.table_name = table_name
        self.parameters = parameters

    def __str__(self):
        return str({
            'table_name': self.table_name,
            'parameters': self.parameters
        })
