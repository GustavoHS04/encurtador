import sqlite3

def create_table() -> None:
    con = sqlite3.connect("data/links.db")
    con.execute("""
CREATE TABLE IF NOT EXISTS links (
    codigo  TEXT PRIMARY KEY CHECK(length(codigo) <= 12),
    url     TEXT NOT NULL    CHECK(length(url) <= 2048),
    acessos INTEGER
);""")

    con.close()

if __name__ == "__main__":
    create_table()