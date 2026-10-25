from pydantic import BaseModel, HttpUrl

class NovoLink(BaseModel):
    url: HttpUrl