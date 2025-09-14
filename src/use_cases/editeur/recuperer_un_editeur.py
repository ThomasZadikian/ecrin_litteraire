from uuid import UUID
from src.domain.model.editeur import Editeur
from src.domain.repository.editeur_repository import EditeurRepository

class RecupererUnediteur: 
    def __init__(self, editeur_repository: EditeurRepository)-> None: 
        self.editeur_repository = editeur_repository

    async def executer(self, editeur_id: UUID) -> Editeur: 
        editeur = await self.editeur_repository.trouver_par_id(editeur_id)
        return editeur