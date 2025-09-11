from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

from src.domain.model.utilisateur import Utilisateur
from src.domain.model.chapitre import Chapitre
from src.domain.model.commentaire import Commentaire
from src.domain.model.genre import Genre

class Livre(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    titre: str
    contenu: str
    auteur: str
    date_publication: datetime
    date_d_ajout: datetime
    date_de_modification: datetime
    auteur_id: UUID
    auteur: Utilisateur
    chapitre: list[Chapitre]
    commentaire: list[Commentaire]
    genre: list[Genre]

class LivreCreationSchema(BaseModel):
    titre: str
    contenu: str
    auteur: str
    date_publication: datetime
    date_d_ajout: datetime
    date_de_modification: datetime
    auteur_id: UUID
    auteur: Utilisateur
    chapitre: list[Chapitre]
    commentaire: list[Commentaire]
    genre: list[Genre]

class LivreUpdateSchema(BaseModel):
    titre: str | None = None
    contenu: str | None = None

