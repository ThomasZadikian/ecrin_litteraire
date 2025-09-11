from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

from src.domain.model.livre import Livre

class Genre(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    nom: str
    livre: list[Livre]