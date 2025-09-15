from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class EditeurCreationSchema(BaseModel):
    nom: str

class EditeurUpdateSchema(BaseModel):
    nom: str

class Editeur(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    nom: str
    date_modification: datetime