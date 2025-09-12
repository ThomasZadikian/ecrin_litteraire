from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class Commentaire(BaseModel): 
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    contenu: str
    date_creation: datetime
    auteur_id: UUID
    auteur: 'Utilisateur'
    livre_id: UUID
    livre: 'Livre'

class CommentaireCreationSchema(BaseModel): 
    contenu: str

class CommentaireUpdateSchema(BaseModel): 
    contenu: str | None = None