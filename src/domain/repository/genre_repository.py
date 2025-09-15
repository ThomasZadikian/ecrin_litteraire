from abc import ABC, abstractmethod
from src.domain.model.genre import Genre
from uuid import UUID

class GenreRepository(ABC):
    @abstractmethod 
    def sauvegarder(self, genre: Genre)-> None: 
        """Sauvegarde un genre dans le dépôt."""
        pass

    @abstractmethod
    def trouver_par_id(self, genre_id: UUID) -> Genre | None: 
        """Récupère un genre par son identifiant."""
        pass

    @abstractmethod
    def mettre_a_jour(self, genre: Genre) -> Genre | None: 
        """ Met à jour le nom d'un genre """
        pass