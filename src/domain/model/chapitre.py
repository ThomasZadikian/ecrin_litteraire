from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from src.domain.model.livre import Livre

class CreationChapitreSchema(BaseModel): 
    titre: str
    contenu: str
    numero_chapitre: int

class ChapitreUpdateSchema(BaseModel):
    titre: str | None = None 
    contenu: str | None = None
    numero_chapitre: int | None = None

class Chapitre(BaseModel): 
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    titre: str
    contenu: str
    numero_chapitre: int
    date_modification: datetime
    livre_id: UUID
    livre: Livre