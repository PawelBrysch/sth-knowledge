
import psycopg2

#TODO poprawic uzycie tego cm'a w innym miejscu
class DBCursor():
    def __init__(self, creds, db_name):
        self.con = psycopg2.connect(
            database=db_name,
            user=creds["user"],
            password=creds["password"])
        self.cur = self.con.cursor()

    def __enter__(self):
        return (self.cur, self.con)

    def __exit__(self, *args):
        self.cur.close()
        self.con.close()