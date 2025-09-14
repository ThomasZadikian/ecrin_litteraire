import pytest

from src.domain.model.chatbot import ChatBotCreationSchema, ChatBot
from src.use_cases.chatbot.creer_un_chatbot import CreerUnChatBot
from src.use_cases.chatbot.recuperer_un_chatbot import RecupererUnChatBot
from src.infrastructure.persistance.inMemory_repository.in_memory_chatbot_repository import InMemoryChatBotRepository

from tests.factory.chatbot_factory import create_chatbot

@pytest.mark.asyncio

async def test_creer_et_recuperer_un_chatbot():
    nouveau_chatbot: ChatBotCreationSchema = create_chatbot()

    repo = InMemoryChatBotRepository()
    creer_un_chatbot = CreerUnChatBot(repo)
    recuperer_un_chatbot = RecupererUnChatBot(repo)

    nouveau_chatbot: ChatBot = await creer_un_chatbot.executer(nouveau_chatbot)
    chatbot_recuperer: ChatBot = await recuperer_un_chatbot.executer(nouveau_chatbot.id)

    assert chatbot_recuperer.id == nouveau_chatbot.id

