import uuid
from datetime import date
from typing import Optional

from src.domain.model.utilisateur import UtilisateurCreationSchema, Utilisateur
from src.domain.model.livre import Livre
from src.domain.model.commentaire import Commentaire
from src.domain.model.roles import Role
from src.domain.model.genre import Genre

Utilisateur.model_rebuild()
Livre.model_rebuild()
Commentaire.model_rebuild()
Role.model_rebuild()
Genre.model_rebuild()

def create_utilisateur(
    prenom: str = "Thomas",
    nom_de_famille: str = "Zadikian",
    date_de_naissance: Optional[date] = None,
    email: str = "thomas@example.com",
    cgu: bool = True,
    rgpd: bool = True,
    cookies: bool = True,
    mot_de_passe: str = "securepassword",
    avatar: Optional[str] = None,

) -> UtilisateurCreationSchema:
    """
    Crée une instance de l'objet Utilisateur pour les tests unitaires.
    """
       
    return UtilisateurCreationSchema(
        id=id,
        prenom=prenom,
        nom_de_famille=nom_de_famille,
        date_de_naissance=date_de_naissance,
        email=email,
        cgu=cgu,
        rgpd=rgpd,
        cookies=cookies,
        mot_de_passe=mot_de_passe,
        avatar=avatar,
    )