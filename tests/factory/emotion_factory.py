import uuid
from datetime import datetime
from typing import Optional

from src.domain.model.emotion import Emotion

def create_emotion(
        id: Optional[uuid.UUID] = None,
        nom: str = "Joie",
        comportement: str = "Exprime la joie de manière chaleureuse et enthousiaste.",
        date_modification: datetime = datetime(2025, 11, 9), 
) -> Emotion:
    """
    Crée une instance de l'objet Emotion pour les tests unitaires.
    """
    if id is None:
        id = uuid.uuid4()
        
    return Emotion(
        id=id,
        nom=nom,
        comportement=comportement,
        date_modification=date_modification
)