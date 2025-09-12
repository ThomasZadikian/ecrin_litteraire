import uuid
from datetime import datetime
from typing import Optional
from src.domain.model.livre import Livre
from src.domain.model.utilisateur import Utilisateur
from src.domain.model.genre import Genre

from tests.factory.user_factory import create_utilisateur

user = create_utilisateur()

def create_livre(
    id: Optional[uuid.UUID] = None,
    titre: str = "Livre",
    contenu: str = "Je suis un contenu de livre",
    date_publication: datetime = datetime(2023, 1, 1),
    date_d_ajout: datetime = datetime(2023, 1, 1),
    date_de_modification: datetime = datetime(2023, 1, 1),
    auteur_id: Optional[uuid.UUID] = None,
    auteur = user,
    genre: Optional[list[Genre]] = None,
) ->Livre :
    """
    Crée une instance de l'objet Livre pour les tests unitaires.
    """
    if id is None:
        id = uuid.uuid4()
        
    return Livre(
        id=id,
        titre=titre,
        contenu=contenu,
        date_publication=date_publication,
        date_d_ajout=date_d_ajout,
        date_de_modification=date_de_modification,
        auteur_id=auteur_id,
        auteur=auteur,
        genre=genre,
    )