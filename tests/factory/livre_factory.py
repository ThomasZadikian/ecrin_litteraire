import uuid
from datetime import datetime, date
from typing import Optional
from src.domain.model.livre import Livre
from src.domain.model.utilisateur import Utilisateur
from src.domain.model.genre import Genre
from tests.factory.user_factory import create_utilisateur
from tests.factory.genre_factory import create_genre

mock_user: Utilisateur = create_utilisateur()
mock_genre : Genre = create_genre()


def create_livre(
    id: Optional[uuid.UUID] = None,
    titre: str = "Livre",
    contenu: str = "Je suis un contenu de livre",
    date_publication: datetime = datetime(2023, 1, 1),
    date_d_ajout: datetime = datetime(2023, 1, 1),
    date_de_modification: datetime = datetime(2023, 1, 1),
    auteur_id: uuid.UUID = mock_user.id,
    auteur: Utilisateur = mock_user,
    genre: list[Genre] = [mock_genre],
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