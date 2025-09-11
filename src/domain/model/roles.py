from pydantic import BaseModel, ConfigDict
from uuid import UUID 
from datetime import datetime

class Role(BaseModel): 
    id: UUID
    nom: str
    date_creation: datetime
    date_modification: datetime
    utilisateur: UUID

class RoleCreateSchema(BaseModel): 
    nom: str

class RoleUpdateSchema(BaseModel): 
    nom: str | None = None
    date_modification: datetime