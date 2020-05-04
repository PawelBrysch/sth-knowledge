import psycopg2
from les_SQL.globals_ import AUTH

# TODO create table

def disconnect_other_sessions(cursor, db_name):
    cursor.execute(f""" 
        SELECT pg_terminate_backend(pid) 
        FROM pg_stat_activity 
        WHERE pid <> pg_backend_pid() AND datname = '{db_name}';
    """)


def make_database_queries_possible(connection):
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)


def create_database(existing_db_name, auth, name):
    con = psycopg2.connect(database=existing_db_name, **auth)
    make_database_queries_possible(con)
    cur = con.cursor()
    cur.execute(f"CREATE DATABASE {name};")
    cur.close()
    con.close()


def drop_database(existing_db_name, auth, name):
    con = psycopg2.connect(database=existing_db_name, **auth)
    make_database_queries_possible(con)
    cur = con.cursor()
    disconnect_other_sessions(cur, name)
    cur.execute(f"DROP DATABASE {name};")
    cur.close()
    con.close()


if __name__ == "__main__":
    a = 1
    create_database("first_db", AUTH, "new_db")
    # drop_database("first_db", AUTH, "new_db")
