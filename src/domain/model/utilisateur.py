from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from src.domain.model.livre import Livre
from src.domain.model.commentaire import Commentaire 
from src.domain.model.roles import Role

class Utilisateur(BaseModel): 
    model_config = ConfigDict(from_attributes=True)
    id : UUID
    prenom : str
    nom_de_famille : str
    email : str
    date_de_naissance : str
    avatar: str
    date_de_creation: datetime
    cgu: bool
    rgpd: bool
    cookies: bool
    date_modification: datetime
    livre: list[Livre]
    commentaire: list[Commentaire]
    auteur_prefere: UUID
    chatbot_prefere: UUID
    role_id: UUID
    role: Role
    
class UtilisateurCreationSchema(BaseModel): 
    prenom : str
    nom_de_famille : str
    email : str
    date_de_naissance : str
    avatar: str
    date_de_creation: datetime
    cgu: bool
    rgpd: bool
    cookies: bool
    mot_de_passe : str 

class UtilisateurUpdateSchema(BaseModel): 
    email : str | None = None
    cgu: bool | None = None
    avatar: str | None = None
    auteur_prefere: UUID
    chatbot_prefere: UUID
    livre: list[Livre]
