from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class Emotion(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    nom: str
    date_modification: datetime