import pytest

from src.domain.model.chatbot import ChatBotUpdateSchema,ChatBot
from src.use_cases.chatbot.creer_un_chatbot import CreerUnChatBot
from src.use_cases.chatbot.recuperer_un_chatbot import RecupererUnChatBot
from src.use_cases.chatbot.modifier_un_chatbot import ModifierUnChatBot
from src.infrastructure.persistance.inMemory_repository.in_memory_chatbot_repository import InMemoryChatBotRepository

from tests.factory.chatbot_factory import create_chatbot

@pytest.mark.asyncio
async def test_mettre_a_jour_un_chatbot(): 

    chatbot_cree = create_chatbot()
    repo = InMemoryChatBotRepository()

    creer_un_chatbot = CreerUnChatBot(repo)
    recuperer_un_chatbot = RecupererUnChatBot(repo)
    modifier_un_chatbot = ModifierUnChatBot(repo)

    nouveau_chatbot: ChatBot = await creer_un_chatbot.executer(chatbot_cree)
    chatbot_recuperer: ChatBot = await recuperer_un_chatbot.executer(nouveau_chatbot.id)
    chatbot_modifier = ChatBotUpdateSchema(nom="Nouveau nom")
    await modifier_un_chatbot.executer(chatbot_recuperer.id, chatbot_modifier)
    chatbot_modifier_recuperer: ChatBot = await recuperer_un_chatbot.executer(chatbot_recuperer.id)

    assert chatbot_modifier_recuperer.nom == "Nouveau nom"