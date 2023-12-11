def sql_gen_delete_by_id_query_based_on_model(model):
    def delete_by_id(id_arg):
        return f'DELETE FROM {model.database_table_name} WHERE id = {id_arg}'

    return delete_by_id
