from uuid import UUID
from src.domain.model.chatbot import ChatBot
from src.domain.repository.chatbot_repository import ChatBotRepository

class RecupererUnChatBot: 
    def __init__(self, chatbot_repository: ChatBotRepository): 
        self.chatbot_repository = chatbot_repository  

    async def executer(self, chatbot_id: UUID) -> ChatBot | None: 
        chatbot = await self.chatbot_repository.trouver_par_id(chatbot_id)
        return chatbot