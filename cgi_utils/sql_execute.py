def sql_execute(con, sql_request: str, get_result: bool = False):
    cursor_obj = con.cursor()
    cursor_obj.execute(sql_request)
    con.commit()
    if get_result:
        return cursor_obj.fetchall()
