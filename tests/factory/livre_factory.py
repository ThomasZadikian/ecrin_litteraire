from uuid import UUID
from datetime import datetime
from typing import Optional
from src.domain.model.livre import LivreCreationSchema
from src.domain.model.utilisateur import Utilisateur
from src.domain.model.genre import Genre
from src.domain.model.livre import Livre
from src.domain.model.commentaire import Commentaire
from src.domain.model.roles import Role

Utilisateur.model_rebuild() 
Livre.model_rebuild()
Commentaire.model_rebuild()
Role.model_rebuild()
Genre.model_rebuild()

def create_livre(
    titre: str = "Titre du Livre",
    contenu_pour_majeur: bool = False,
    date_publication: datetime = datetime.now(),


) ->LivreCreationSchema :
    """
    Crée une instance de l'objet Livre pour les tests unitaires.
    """
    return LivreCreationSchema(
        titre = titre,
        contenu_pour_majeur = contenu_pour_majeur,
        date_publication = date_publication,
    )