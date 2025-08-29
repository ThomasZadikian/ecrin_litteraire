from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class Livre(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    titre: str
    contenu: str
    auteur: str
    date_publication: datetime

class LivreCreationSchema(BaseModel):
    titre: str
    contenu: str
    auteur: str

class LivreUpdateSchema(BaseModel):
    titre: str | None = None
    contenu: str | None = None
    auteur: str | None = None
