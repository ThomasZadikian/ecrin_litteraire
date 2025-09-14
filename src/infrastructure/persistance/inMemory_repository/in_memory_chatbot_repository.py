from uuid import UUID
from src.domain.model.chatbot import ChatBot, ChatBotUpdateSchema

class InMemoryChatBotRepository: 
    def __init__(self) -> None:
        self.data: dict[UUID, ChatBot] = {}

    async def sauvegarder(self, chatbot: ChatBot)-> None: 
        self.data[chatbot.id] = chatbot

    async def trouver_par_id(self, chatbot_id : UUID)-> ChatBot: 
        return self.data.get(chatbot_id)
    
    async def mettre_a_jour(
            self, 
            chatbot_data: ChatBotUpdateSchema
    ) -> ChatBot | None: 
        if chatbot_data.id in self.data: 
            self.data[chatbot_data.id] = chatbot_data