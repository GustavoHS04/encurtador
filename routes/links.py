from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse

from schemas import NovoLink
from queries.queries import inserir_link, buscar_link
from services.codigo import gerar_codigo

router = APIRouter()

@router.post("/encurtar")
def encurtar(novo: NovoLink, tam: int = Query(6, ge=4, le=12)) -> dict[str,str]:
    codigo = gerar_codigo(tam)
    inserir_link(codigo, str(novo.url))

    return {"codigo": codigo, "link_curto": f"http://127.0.0.1/{codigo}"}

@router.get("/{codigo}")
def acessar(codigo: str) -> RedirectResponse:
    link_original = buscar_link(codigo)

    if link_original is None:
        raise HTTPException(status_code=404, detail="Link não encontrado")
        
    return RedirectResponse(link_original)
