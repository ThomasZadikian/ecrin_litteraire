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
    
    def mettre_a_jour(self, livre: Livre) -> None: 
        """
        Met à jour un livre existant dans le dépôt en mémoire.
        Args:
            livre (Livre): Le livre à mettre à jour.
        """
        if livre.id in self.data:
            self.data[livre.id] = livre

    def supprimer(self, id: UUID) -> None:
        """
        Supprime un livre du dépôt en mémoire par son identifiant.
        Args:
            id (UUID): L'identifiant du livre à supprimer.
        """
        if id in self.data:
            del self.data[id]