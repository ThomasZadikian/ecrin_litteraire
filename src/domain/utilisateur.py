from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class Utilisateur(BaseModel): 
    model_config = ConfigDict(from_attributes=True)
    id : UUID
    prenom : str
    nom_de_famille : str
    date_de_naissance : datetime
    email : str
    
class UtilisateurCreationSchema(BaseModel): 
    prenom : str
    nom_de_famille : str
    date_de_naissance : datetime
    email : str
    mot_de_passe : str