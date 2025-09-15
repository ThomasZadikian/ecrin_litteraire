from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime


class LivreCreationSchema(BaseModel):
    titre: str
    contenu_pour_majeur: bool
    date_publication: datetime 


class LivreUpdateSchema(BaseModel):
    titre: str | None = None

class Livre(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    titre: str
    contenu_pour_majeur: bool
    date_publication: datetime
    date_d_ajout: datetime
    date_de_modification: datetime
    auteur_id: UUID 
    auteur: 'Utilisateur'
    genre: 'Genre' 
 
