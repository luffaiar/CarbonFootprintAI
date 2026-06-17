import sqlite3

def create_table():

    conn = sqlite3.connect("carbon.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        date TEXT,
        score REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_data(date, score):

    conn = sqlite3.connect("carbon.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history(date, score) VALUES (?, ?)",
        (date, score)
    )

    conn.commit()
    conn.close()