from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class PersonaCreationSchema(BaseModel): 
    nom: str

class PersonaUpdateSchema(BaseModel):
    nom:str

class Persona(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    nom: str
    date_modification: datetime