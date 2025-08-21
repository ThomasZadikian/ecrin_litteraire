from uuid import UUID
from src.domain.livre import Livre
from src.domain.livre_repository import LivreRepository

class InMemoryLivreRepository(LivreRepository): 

    def __init__(self):
        self.data: dict[UUID, Livre] = {}

    def sauvegarder(self, livre):
        """
        Sauvegarde un livre dans le dépôt en mémoire.
        Args:
            livre (Livre): Le livre à sauvegarder.
        """
        self.data[livre.id] = livre

    def trouver_par_id(self, id):
        """
        Trouve un livre par son identifiant dans le dépôt en mémoire.
        Args:
            id (UUID): L'identifiant du livre à trouver.
        Returns:
            Livre | None: Le livre trouvé ou None si non trouvé.
        """
        return self.data.get(id)