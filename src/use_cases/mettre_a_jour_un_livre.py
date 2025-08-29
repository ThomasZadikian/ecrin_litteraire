from uuid import UUID
from src.domain.livre import Livre, LivreUpdateSchema
from src.domain.livre_repository import LivreRepository

class MettreAJourUnLivre:
    def __init__(self, livre_repository: LivreRepository):
        self.livre_repository = livre_repository

    async def executer(self, livre_id: UUID, livre_data: LivreUpdateSchema) -> Livre | None:
        livre = await self.livre_repository.trouver_par_id(livre_id)
        if not livre:
            return None

        update_data = livre_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(livre, key, value)
            
        await self.livre_repository.mettre_a_jour(livre)
        
        livre_a_jour = await self.livre_repository.trouver_par_id(livre_id)
        return livre_a_jour