from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from uuid import UUID

class ChatBot(BaseModel): 
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    nom: str
    utilisateur: list['Utilisateur']