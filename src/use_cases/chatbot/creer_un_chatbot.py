import uuid
from datetime import datetime

from src.domain.model.chatbot import ChatBot, ChatBotCreationSchema
from src.domain.repository.chatbot_repository import ChatBotRepository

class CreerUnChatBot: 
    def __init__ (self, chatbot_repository: ChatBotRepository)-> None: 
        self.chatbot_repository = chatbot_repository

    async def executer(
            self, 
            chatbot_data: ChatBotCreationSchema,
            ) -> ChatBot: 
        nouveau_chatbot= ChatBot(
            id = uuid.uuid4(),
            nom = chatbot_data.nom, 
        )
        await self.chatbot_repository.sauvegarder(nouveau_chatbot)
        return nouveau_chatbot

