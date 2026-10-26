from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse

from schemas import NovoLink
from queries.queries import (
    inserir_link, buscar_link, registrar_acesso,
    buscar_acessos, buscar_top_acessos

)
from services.codigo import gerar_codigo
from services.hosts import host_proibido

router = APIRouter()

@router.post("/encurtar")
def encurtar(novo: NovoLink, tam: int = Query(6, ge=4, le=12)) -> dict[str,str]:
    if host_proibido(novo.url.host):
        raise HTTPException(status_code=422, detail="Não é possível encurtar links que apontem para o próprio serviço")

    codigo = gerar_codigo(tam)
    inserir_link(codigo, str(novo.url))

    return {"codigo": codigo, "link_curto": f"http://127.0.0.1/{codigo}"}

@router.get("/top")
def top_acessos(limite: int = Query(5, ge=1, le=50)):
    ranking = buscar_top_acessos(limite)

    if top_acessos is None:
        raise HTTPException(status_code=404, detail="Nenhum link encontrado")

    return [{"codigo": c, "url": u, "acessos": a} for c, u, a in ranking]
    
@router.get("/estatisticas/{codigo}")
def estatistica_link(codigo: str) -> dict[str, str | int]:
    acessos = buscar_acessos(codigo)

    if acessos is None:
        raise HTTPException(status_code=404, detail="Link não encontrado")

    return {"codigo": acessos[0], "link": acessos[1], "acessos": acessos[2]}

@router.get("/{codigo}")
def acessar(codigo: str) -> RedirectResponse:
    link_original = buscar_link(codigo)

    if link_original is None:
        raise HTTPException(status_code=404, detail="Link não encontrado")

    registrar_acesso(codigo)
    return RedirectResponse(link_original)

