from abc import ABC, abstractmethod
from src.domain.model.emotion import Emotion
from uuid import UUID

class EmotionRepository(ABC):
    @abstractmethod 
    def sauvegarder(self, emotion: Emotion)-> None: 
        """Sauvegarde un emotion dans le dépôt."""
        pass

    @abstractmethod
    def trouver_par_id(self, emotion_id: UUID) -> Emotion | None: 
        """Récupère un emotion par son identifiant."""
        pass

    @abstractmethod
    def mettre_a_jour(self, emotion: Emotion) -> Emotion | None: 
        """ Met à jour le nom d'un emotion """
        pass