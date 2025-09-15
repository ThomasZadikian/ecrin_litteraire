import uuid
from datetime import datetime
from typing import Optional

from src.domain.model.emotion import EmotionCreationSchema

def create_emotion(
        nom: str = "Test",
        comportement: str = "Tu es une emotion de test. Comporte toi comme un robot idiot.",
) -> EmotionCreationSchema:
    """
    Crée une instance de l'objet Emotion pour les tests unitaires.
    """

    return EmotionCreationSchema(
        nom=nom,
        comportement=comportement
)