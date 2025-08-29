from uuid import UUID
from src.domain.livre import Livre
from src.domain.livre_repository import LivreRepository

class InMemoryLivreRepository(LivreRepository):
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
        
    async def mettre_a_jour(self, livre: Livre) -> None:
        if livre.id in self._data:
            self._data[livre.id] = livre

    async def supprimer(self, livre: Livre) -> None:
        if livre.id in self._data:
            del self._data[livre.id]