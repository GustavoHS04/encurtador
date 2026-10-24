import random
import string

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from queries.queries import inserir_link, buscar_link

ALFABETO = string.ascii_letters + string.digits
app = FastAPI()

class NovoLink(BaseModel):
    url: str



def gerar_codigo(tam: int) -> str:
    codigo = "".join(random.choices(ALFABETO, k=tam))

    return codigo if buscar_link(codigo) is None else gerar_codigo(tam)
    
@app.post("/encurtar")
def encurtar(novo: NovoLink, tam: int = Query(6, ge=4, le=12)) -> dict[str,str]:
    codigo = gerar_codigo(tam)
    inserir_link(codigo, novo.url)

    return {"codigo": codigo, "link_curto": f"http://127.0.0.1/{codigo}"}

@app.get("/{codigo}")
def acessar(codigo: str) -> RedirectResponse:
    link_original = buscar_link(codigo)

    if link_original is None:
        raise HTTPException(status_code=404, detail="Link não encontrado")
        
    return RedirectResponse(link_original)

