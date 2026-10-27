from .connect_db import connect

def create_links() -> None:
    con = connect()
    con.execute("""
CREATE TABLE IF NOT EXISTS links (
    codigo  TEXT PRIMARY KEY CHECK(length(codigo) <= 12),
    url     TEXT NOT NULL    CHECK(length(url) <= 2048)
);""")

    con.close()

def create_acessos() -> None:
    con = connect()
    con.execute("""
CREATE TABLE IF NOT EXISTS acessos (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo    TEXT    NOT NULL REFERENCES links(codigo),
    data_hora TEXT    NOT NULL DEFAULT(CURRENT_TIMESTAMP)
);""")

    con.execute("""CREATE INDEX IF NOT EXISTS idx_acessos_codigo ON acessos(codigo)""")

    con.close()