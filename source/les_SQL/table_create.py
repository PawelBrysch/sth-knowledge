import psycopg2
from les_SQL.globals_ import AUTH
import pandas as pd


# TODO wczytaj dane z csv

def create_table(db_name, table_name, columns, auth):
    con = psycopg2.connect(database=db_name, **auth)
    cur = con.cursor()

    cur.execute(f"CREATE TABLE {table_name} ({', '.join(columns)});")
    con.commit()

    cur.close()
    con.close()


def create_empty_table(path_to_data, table_name, db_name, auth):
    dataframe = pd.read_csv(path_to_data)
    columns = ["id serial PRIMARY KEY"]
    for name, data_type in zip(dataframe.columns.str.strip(), dataframe.iloc[0]):
        columns.append(f"{name} {data_type}")
    create_table(db_name, table_name, columns, auth)



def insert_from_csv(table_name, path_to_data, db_name, auth):
    dataframe = pd.read_csv(path_to_data)
    column_names = dataframe.columns.str.strip()
    number_of_rows = dataframe.shape[0]

    con = psycopg2.connect(database=db_name, **auth)
    cur = con.cursor()

    query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES "
    for idx in range(1, number_of_rows):
        row = dataframe.iloc[idx]
        part = "', '".join(list(row.str.strip()))
        record = f"(\'{part}\')"
        cur.execute(query + record)

    con.commit()
    cur.close()
    con.close()

def create_table_from_csv(path_to_data, table_name, db_name, auth):
    create_empty_table(path_to_data, table_name, db_name, auth)
    insert_from_csv(table_name, path_to_data, db_name, auth)


if __name__ == "__main__":
    a = 1
    # create_empty_table(
    #     path_to_data=rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\les_SQL\st.csv",
    #     table_name="from_csv",
    #     db_name="new_db",
    #     auth=AUTH)

    # create_table(
    #     db_name="new_db",
    #     auth=AUTH,
    #     table_name="test5",
    #     columns=[
    #         "id serial PRIMARY KEY",
    #         "name text",
    #         "age integer"
    #     ])

    # insert_from_csv(
    #     db_name="new_db",
    #     table_name="from_csv",
    #     auth=AUTH,
    #     path_to_data=rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\les_SQL\st.csv",
    # )

    # create_table_from_csv(
    #     db_name="new_db",
    #     table_name="from_csv",
    #     auth=AUTH,
    #     path_to_data=rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\les_SQL\st.csv",
    # )