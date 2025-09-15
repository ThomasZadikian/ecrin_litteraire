from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional


class UtilisateurCreationSchema(BaseModel): 
    prenom : str
    nom_de_famille : str
    date_de_naissance : datetime | None = None
    email : str 
    cgu: bool
    rgpd: bool
    cookies: bool
    mot_de_passe : str 
    avatar: str | None = None

class UtilisateurUpdateSchema(BaseModel):
    email: Optional[str] = None
    avatar: Optional[str] = None
    auteur_prefere_id: Optional[UUID] = None
    chatbot_prefere_id: Optional[UUID] = None

class Utilisateur(BaseModel): 
    model_config = ConfigDict(from_attributes=True)
    id : UUID
    prenom : str
    nom_de_famille : str
    date_de_naissance : datetime | None = None
    email : str
    avatar: str | None = None
    date_de_creation_du_compte: datetime
    date_de_modification : datetime
    cgu: bool
    rgpd: bool
    cookies: bool
    livre: list['Livre'] | None = None
    commentaire: list['Commentaire'] | None = None
    auteur_prefere_id: UUID | None = None   
    chatbot_prefere_id: UUID | None = None
    role_id: UUID
