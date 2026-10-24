import sqlite3

def create_table() -> None:
    con = sqlite3.connect("data/links.db")
    con.execute("""\
CREATE TABLE IF NOT EXISTS links (
    codigo  varchar(12)      PRIMARY KEY,
    url     varchar(2048)    NOT NULL
);""")

    con.close()

if __name__ == "__main__":
    create_table()