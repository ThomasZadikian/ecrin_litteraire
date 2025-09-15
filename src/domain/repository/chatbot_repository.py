from uuid import UUID
from abc import ABC, abstractmethod
from datetime import datetime 

from src.domain.model.chatbot import ChatBot, ChatBotUpdateSchema

class ChatBotRepository: 
    @abstractmethod
    async def sauvegarder(self, chatbot: ChatBot)-> None: 
        """Sauvegarder un chatbot """
        pass

    @abstractmethod
    async def trouver_par_id(self, chatbot_id: UUID) -> ChatBot: 
        """ Trouver un chatbot avec un ID """
        pass

    @abstractmethod
    async def mettre_a_jour(
        self, 
        chatbot_modifier: ChatBotUpdateSchema)-> ChatBot | None:
        """Modifier un chatbot"""
        pass
