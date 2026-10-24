import sqlite3

def inserir_link(codigo: str, url: str) -> None:
    con = sqlite3.connect("data/links.db")

    con.execute("INSERT INTO links VALUES (?, ?);", (codigo, url))
    con.commit()

    con.close()

def buscar_link(codigo: str) -> str | None:
    con = sqlite3.connect("data/links.db")

    resultado = con.execute("""
        SELECT url FROM links
        WHERE codigo = ?
        """, (codigo,)
    ).fetchone()
    con.close()

    if resultado is None:
        return None
    
    return resultado[0]