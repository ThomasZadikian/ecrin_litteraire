from abc import ABC, abstractmethod
from src.domain.livre import Livre
from uuid import UUID

class LivreRepository(ABC):
    """
    Interface pour le dépôt de livres.
    """
    @abstractmethod
    def sauvegarder(self, livre : Livre) -> None:
        """Sauvegarde un livre dans le dépôt."""
        pass

    @abstractmethod
    def trouver_par_id(self, id : UUID) -> Livre | None:
        """Trouve un livre par son identifiant."""
        pass


