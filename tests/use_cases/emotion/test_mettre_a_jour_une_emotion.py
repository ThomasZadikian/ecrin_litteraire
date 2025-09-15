import pytest

from src.domain.model.emotion import EmotionUpdateSchema, Emotion
from src.use_cases.emotion.creer_une_emotion import CreerUneEmotion
from src.use_cases.emotion.recuperer_une_emotion import RecupererUneEmotion
from src.use_cases.emotion.modifier_une_emotion import ModifierUneEmotion
from src.infrastructure.persistance.inMemory_repository.in_memory_emotion_repository import InMemoryEmotionRepository

from tests.factory.emotion_factory import create_emotion

@pytest.mark.asyncio
async def test_mettre_a_jour_une_emotion(): 

    emotion_cree = create_emotion()
    repo = InMemoryEmotionRepository()

    creer_un_emotion = CreerUneEmotion(repo)
    recuperer_un_emotion = RecupererUneEmotion(repo)
    modifier_un_emotion = ModifierUneEmotion(repo)

    nouveau_emotion: Emotion = await creer_un_emotion.executer(emotion_cree)
    emotion_recuperer: Emotion = await recuperer_un_emotion.executer(nouveau_emotion.id)
    emotion_modifier = EmotionUpdateSchema(
        nom="emotion de test unitaire",
        comportement="Comportement de test unitaire"
        )
    await modifier_un_emotion.executer(emotion_recuperer.id, emotion_modifier)
    emotion_modifier_recuperer: Emotion = await recuperer_un_emotion.executer(emotion_recuperer.id)

    assert emotion_modifier_recuperer.id == emotion_recuperer.id
    assert emotion_modifier_recuperer.nom == "emotion de test unitaire"
    assert emotion_modifier_recuperer.comportement == "Comportement de test unitaire"