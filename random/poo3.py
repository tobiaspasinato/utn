def get_connetion():
    lista = []
    conn = sql.connect("netflix_oscar.db")
    cur = conn.cursor()
    lista.append()
    return conn, cur