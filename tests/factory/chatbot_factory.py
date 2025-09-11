import uuid
from datetime import datetime, date, timezone
from typing import Optional
from src.domain.model.utilisateur import Utilisateur
from src.domain.model.chatbot import ChatBot
from tests.factory.user_factory import create_utilisateur

mock_utilisateur : Utilisateur = create_utilisateur()
mock_utilisateur_2 : Utilisateur = create_utilisateur()

mock_list_utilisateur: list[Utilisateur] = [mock_utilisateur, mock_utilisateur_2]

def create_chatbot(
        id: Optional[uuid.UUID] = None,
        nom: str = "Chatbot Par Défaut",
        utilisateur: Optional[list[Utilisateur]] = mock_list_utilisateur
) -> ChatBot:
    """
    Crée une instance de l'objet ChatBot pour les tests unitaires.
    """
    if id is None:
        id = uuid.uuid4()
        
    return ChatBot(
        id=id,
        nom=nom,
        utilisateur=utilisateur
    )