from uuid import UUID
from domain.model.livre import Livre

class InMemoryLivreRepository:
    """
    Implémentation en mémoire du repository, utilisée pour les tests.
    Toutes les méthodes doivent être asynchrones pour respecter l'interface.
    """
    def __init__(self):
        self._data: dict[UUID, Livre] = {}

    async def sauvegarder(self, livre: Livre) -> None:
        self._data[livre.id] = livre

    async def trouver_par_id(self, livre_id: UUID) -> Livre | None:
        return self._data.get(livre_id)
    
    async def trouver_par_auteur(self, auteur: str) -> list[Livre]:
        """
        Trouve tous les livres d'un auteur donné.
        Retourne une liste vide si aucun livre n'est trouvé.
        """
        livres_trouves = [
            livre for livre in self._data.values()
            if livre.auteur == auteur
        ]
        return livres_trouves
        
    async def mettre_a_jour(self, livre: Livre) -> None:
        if livre.id in self._data:
            self._data[livre.id] = livre

    async def supprimer(self, livre: Livre) -> None:
        if livre.id in self._data:
            del self._data[livre.id]