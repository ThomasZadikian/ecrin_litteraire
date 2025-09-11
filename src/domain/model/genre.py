from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

from src.domain.model.livre import Livre

class Genre(BaseModel):
    id: UUID
    nom: str
    livre: list[Livre]