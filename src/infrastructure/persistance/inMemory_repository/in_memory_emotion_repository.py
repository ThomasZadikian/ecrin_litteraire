from uuid import UUID
from src.domain.model.emotion import Emotion

class InMemoryEmotionRepository:
    def __init__ (self): 
        self.data: dict[UUID, Emotion] = {}

    async def sauvegarder(self, emotion: Emotion) -> None: 
        self.data[emotion.id] = emotion

    async def trouver_par_id(self, emotion_id: UUID) -> Emotion | None: 
        return self.data.get(emotion_id)
    
    async def mettre_a_jour(self, emotion: Emotion) -> Emotion | None: 
         if emotion.id in self.data:
            self.data[emotion.id] = emotion