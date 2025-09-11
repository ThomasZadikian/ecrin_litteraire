from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class Editeur(BaseModel):
    id: UUID
    nom: str
    date_modification: datetime