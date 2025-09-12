import uuid
from typing import Optional

from src.domain.model.utilisateur import Utilisateur
from src.domain.model.chatbot import ChatBot

def create_chatbot(
        id: Optional[uuid.UUID] = None,
        nom: str = "Chatbot Par Défaut",
        utilisateur: Optional[list[Utilisateur]] = None
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