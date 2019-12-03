import psycopg2

con = psycopg2.connect(
    # host = ""
    database="first_db",
    user="devoted",
    password="Janina123")
cur = con.cursor()



cur.execute("SELECT id, name FROM employee")
rows = cur.fetchall()


'''# Dopiero wtedy inserty dzialaja.'''
# con.commit()


cur.close()
con.close()


for r in rows:
    print(f"id {r[0]}, name {r[1]}")