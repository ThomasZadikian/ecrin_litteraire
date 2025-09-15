from uuid import UUID
from src.domain.model.emotion import Emotion
from src.domain.repository.emotion_repository import EmotionRepository

class RecupererUneEmotion: 
    def __init__(self, emotion_repository: EmotionRepository): 
        self.emotion_repository = emotion_repository  

    async def executer(self, emotion_id: UUID) -> Emotion | None: 
        emotion = await self.emotion_repository.trouver_par_id(emotion_id)
        return emotion