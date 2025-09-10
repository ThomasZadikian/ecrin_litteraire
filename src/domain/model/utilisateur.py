from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class Utilisateur(BaseModel): 
    model_config = ConfigDict(from_attributes=True)
    id : UUID
    prenom : str
    nom_de_famille : str
    date_de_naissance : str
    email : str

    def __init__(self, id, email, mot_de_passe_hash):
        self.id = id
        self.email = email
        self.mot_de_passe_hash = mot_de_passe_hash

    def __repr__(self):
        return f"<Utilisateur(id='{self.id}', email='{self.email}')>"
    
class UtilisateurCreationSchema(BaseModel): 
    prenom : str
    nom_de_famille : str
    date_de_naissance : str
    email : str
    mot_de_passe : str 