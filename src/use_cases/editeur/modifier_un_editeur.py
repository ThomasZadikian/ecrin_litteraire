from uuid import UUID
from src.domain.model.editeur import Editeur, EditeurUpdateSchema
from src.domain.repository.editeur_repository import EditeurRepository

class ModifierUnediteur: 
    def __init__(self, editeur_repository: EditeurRepository):
        self.editeur_repository = editeur_repository

    async def executer(self, editeur_id: UUID, editeur_data: EditeurUpdateSchema) -> Editeur: 
        editeur = await self.editeur_repository.trouver_par_id(editeur_id)

        if not editeur:  
            return None
        
        update_data = editeur_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(editeur, key, value)

        editeur_a_jour = await self.editeur_repository.mettre_a_jour(editeur)
        return editeur_a_jour
