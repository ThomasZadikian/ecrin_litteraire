import uuid
from typing import Optional

from src.domain.model.utilisateur import Utilisateur
from src.domain.model.chatbot import ChatBotCreationSchema

def create_chatbot(
        nom: str = "Chatbot Par Défaut",
) -> ChatBotCreationSchema:
    """
    Crée une instance de l'objet ChatBot pour les tests unitaires.
    """

    return ChatBotCreationSchema(
        nom=nom,
    )