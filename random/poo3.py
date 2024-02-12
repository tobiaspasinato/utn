import sqlite3

def get_connetion():
    lista = []
    conn = sqlite3.connect("netflix_oscar.db")
    cur = conn.cursor()
    lista.append()
    return conn, cur