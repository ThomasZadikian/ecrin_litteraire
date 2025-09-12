import uuid
from datetime import datetime
from typing import Optional
from src.domain.model.utilisateur import Utilisateur
from src.domain.model.livre import Livre
from src.domain.model.commentaire import Commentaire
from tests.factory.user_factory import create_utilisateur
from tests.factory.livre_factory import create_livre

mock_utilisateur : Utilisateur = create_utilisateur()
mock_livre : Livre = create_livre()

def create_commentaire(
        id: Optional[uuid.UUID] = None, 
        contenu: str = "Commentaire de test", 
        date_creation: datetime = datetime(2025, 11, 9),
        auteur_id: uuid.UUID = mock_utilisateur.id,
        auteur : Optional[Utilisateur] = None,
        livre_id: Optional[uuid.UUID] = None,
        livre : Optional[Livre] = None
) -> Commentaire : 
    """
    Crée une instance de l'objet Commentaire pour les tests unitaires.
    """
    if id is None:
        id = uuid.uuid4()
        
    return Commentaire(
        id=id,
        contenu=contenu,
        date_creation=date_creation,
        auteur_id=auteur_id,
        auteur=auteur,
        livre_id=livre_id,
        livre=livre
    )