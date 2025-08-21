from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Livre(BaseModel):
    id: UUID
    titre: str
    contenu: str
    auteur: str
    date_publication: datetime

class LivreCreationSchema(BaseModel):
    titre: str
    contenu: str
    auteur: str
