from abc import ABC, abstractmethod
from src.domain.model.persona import Persona
from uuid import UUID

class PersonaRepository(ABC):
    @abstractmethod 
    def sauvegarder(self, persona: Persona)-> None: 
        """Sauvegarde un persona dans le dépôt."""
        pass

    @abstractmethod
    def trouver_par_id(self, persona_id: UUID) -> Persona | None: 
        """Récupère un persona par son identifiant."""
        pass

    @abstractmethod
    def mettre_a_jour(self, persona: Persona) -> Persona | None: 
        """ Met à jour le nom d'un persona """
        pass