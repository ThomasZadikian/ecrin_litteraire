from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

from src.domain.model.livre import Livre
from src.domain.model.utilisateur import Utilisateur

class Commentaire(BaseModel): 
    id: UUID
    contenu: str
    date_creation: datetime
    auteur_id: UUID
    auteur: Utilisateur
    livre_id: UUID
    livre: Livre

class CommentaireCreationSchema(BaseModel): 
    contenu: str

class CommentaireUpdateSchema(BaseModel): 
    contenu: str | None = None