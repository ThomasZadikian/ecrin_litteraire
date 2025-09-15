from uuid import UUID
from src.domain.model.emotion import Emotion, EmotionUpdateSchema
from src.domain.repository.emotion_repository import EmotionRepository

class ModifierUneEmotion:
    def __init__(self, emotion_repository: EmotionRepository): 
        self.emotion_repository = emotion_repository
    
    async def executer(self, emotion_id: UUID, emotion_data: EmotionUpdateSchema) -> Emotion : 
        emotion = await self.emotion_repository.trouver_par_id(emotion_id)

        if not emotion:
            return None
        
        update_data = emotion_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(emotion, key, value) 

        emotion_a_jour = await self.emotion_repository.mettre_a_jour(emotion)
        return emotion_a_jour