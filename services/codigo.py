import random
import string

from queries.queries import buscar_link

ALFABETO = string.ascii_letters + string.digits


def gerar_codigo(tam: int) -> str:
    codigo = "".join(random.choices(ALFABETO, k=tam))

    return codigo if buscar_link(codigo) is None else gerar_codigo(tam)