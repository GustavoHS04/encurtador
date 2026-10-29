from ..database.connect_db import connect

def inserir_link(codigo: str, url: str) -> None:
    con = connect()

    con.execute("INSERT INTO links VALUES (?, ?, 0);", (codigo, url))
    con.commit()

    con.close()

def registrar_acesso(codigo: str) -> None:
    con = connect()

    with con:
        con.execute("UPDATE links SET acessos = acessos + 1 WHERE codigo = ?", (codigo,))
        con.execute("INSERT INTO acessos (codigo) VALUES (?)", (codigo,))

    con.close()

def buscar_link(codigo: str) -> str | None:
    con = connect()

    resultado = con.execute("""
        SELECT url FROM links
        WHERE codigo = ?
        """, (codigo,)
    ).fetchone()
    con.close()

    if resultado is None:
        return None
    
    return resultado[0]

def buscar_acessos(codigo: str) -> tuple[str, str, str | int] | None:
    con = connect()

    resultado = con.execute("""
        SELECT codigo, url, acessos
        FROM links
        WHERE codigo = ?
    """, (codigo,)
    ).fetchone()
    con.close()

    return resultado

def buscar_top_acessos(limite: int = 5) -> list[str] | None:
    con = connect()

    resultado = con.execute("""
        SELECT codigo, url, acessos
        FROM links
        ORDER BY acessos DESC, codigo
        LIMIT ?
    """, (limite,)
    ).fetchall()
    con.close()

    return resultado