from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

from src.domain.model.utilisateur import Utilisateur
from src.domain.model.livre import Livre

class Commentaire(BaseModel): 
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    contenu: str
    date_creation: datetime
    auteur_id: UUID
    auteur: Utilisateur
    livre_id: UUID
    livre: Livre

class CommentaireCreationSchema(BaseModel): 
    contenu: str
    date_creation: datetime

class CommentaireUpdateSchema(BaseModel): 
    contenu: str | None = None