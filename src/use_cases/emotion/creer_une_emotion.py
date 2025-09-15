import uuid
from datetime import datetime

from src.domain.model.emotion import Emotion, EmotionCreationSchema
from src.domain.repository.emotion_repository import EmotionRepository

class CreerUneEmotion: 
    def __init__(self, emotion_repository: EmotionRepository):
        self.emotion_repository = emotion_repository  

    async def executer(self, emotion_data: EmotionCreationSchema) -> Emotion: 
        nouveau_emotion = Emotion(
            id = uuid.uuid4(), 
            nom = emotion_data.nom,
            comportement=emotion_data.comportement,
            date_modification=datetime.now()
        )
        await self.emotion_repository.sauvegarder(nouveau_emotion)
        return nouveau_emotion