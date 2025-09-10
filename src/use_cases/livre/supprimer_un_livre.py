from uuid import UUID
from src.domain.repository.livre_repository import LivreRepository
from src.domain.exceptions import LivreNotFoundError

class SupprimerUnLivre:
    def __init__(self, livre_repository: LivreRepository):
        self.livre_repository = livre_repository

    async def executer(self, livre_id: UUID) -> None:
        livre_a_supprimer = await self.livre_repository.trouver_par_id(livre_id)
        if not livre_a_supprimer:
            raise LivreNotFoundError(f"Livre avec l'id : {livre_id} non trouvé")
        
        await self.livre_repository.supprimer(livre_a_supprimer)