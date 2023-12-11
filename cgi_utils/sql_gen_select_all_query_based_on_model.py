def sql_gen_select_all_query_based_on_model(model):
    return f'SELECT * FROM {model.database_table_name}'