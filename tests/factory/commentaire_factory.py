import uuid
from datetime import datetime
from typing import Optional
from src.domain.model.utilisateur import Utilisateur
from src.domain.model.livre import Livre
from src.domain.model.commentaire import CommentaireCreationSchema
from tests.factory.user_factory import create_utilisateur
from tests.factory.livre_factory import create_livre

mock_utilisateur : Utilisateur = create_utilisateur()
mock_livre : Livre = create_livre()

def create_commentaire(
        contenu: str = "Commentaire de test", 
        date_creation: datetime = datetime.now(),
) -> CommentaireCreationSchema : 
    """
    Crée une instance de l'objet Commentaire pour les tests unitaires.
    """
        
    return CommentaireCreationSchema(
        contenu=contenu,
        date_creation=date_creation,
    )