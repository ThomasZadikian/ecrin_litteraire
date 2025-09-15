import pytest

from src.domain.model.emotion import EmotionCreationSchema, Emotion
from src.use_cases.emotion.creer_une_emotion import CreerUneEmotion
from src.use_cases.emotion.recuperer_une_emotion import RecupererUneEmotion
from src.infrastructure.persistance.inMemory_repository.in_memory_emotion_repository import InMemoryEmotionRepository

from tests.factory.emotion_factory import create_emotion

@pytest.mark.asyncio

async def test_creer_et_recuperer_une_emotion():
    nouveau_emotion: EmotionCreationSchema = create_emotion()

    repo = InMemoryEmotionRepository()
    creer_un_emotion = CreerUneEmotion(repo)
    recuperer_un_emotion = RecupererUneEmotion(repo)

    nouveau_emotion: Emotion = await creer_un_emotion.executer(nouveau_emotion)
    emotion_recuperer: Emotion = await recuperer_un_emotion.executer(nouveau_emotion.id)

    assert emotion_recuperer.id == nouveau_emotion.id

