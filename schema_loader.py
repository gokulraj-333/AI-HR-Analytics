from sql_executor import run_query

def get_schema():

    query = """
    SELECT
        TABLE_NAME,
        COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA='HRAnalytics'
    ORDER BY TABLE_NAME, ORDINAL_POSITION;
    """

    columns, rows = run_query(query)

    schema = ""

    current_table = ""

    for table, column in rows:

        if table != current_table:
            current_table = table
            schema += f"\nTable: {table}\n"

        schema += f"- {column}\n"

    return schema