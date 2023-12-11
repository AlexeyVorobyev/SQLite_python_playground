def sql_gen_insert_based_on_model(model):
    def post(model_instance):
        model_instance_dict: dict = model_instance.to_dict()
        model_columns = str([key for key in model_instance_dict.keys()]).strip('[]')
        model_values = str([value for value in model_instance_dict.values()]).strip('[]')
        return (f'INSERT INTO {model.database_table_name} ({model_columns})\n'
                f'VALUES ({model_values})')

    return post
