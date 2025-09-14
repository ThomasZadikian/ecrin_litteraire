from uuid import UUID
from src.domain.model.chatbot import ChatBot, ChatBotUpdateSchema
from src.domain.repository.chatbot_repository import ChatBotRepository

class ModifierUnChatBot:
    def __init__(self, chatbot_repository: ChatBotRepository): 
        self.chatbot_repository = chatbot_repository
    
    async def executer(self, chatbot_id: UUID, chatbot_data: ChatBotUpdateSchema) -> ChatBot : 
        chatbot = await self.chatbot_repository.trouver_par_id(chatbot_id)

        if not chatbot:
            return None
        
        update_data = chatbot_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(chatbot, key, value) 

        chatbot_a_jour = await self.chatbot_repository.mettre_a_jour(chatbot)
        return chatbot_a_jour