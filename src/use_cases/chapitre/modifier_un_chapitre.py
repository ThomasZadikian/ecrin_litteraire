from uuid import UUID
from src.domain.model.chapitre import Chapitre, ChapitreUpdateSchema
from src.domain.repository.chapitre_repository import ChapitreRepository

class ModifierUnChapitre: 
    def __init__(self, chapitre_repository: ChapitreRepository):
        self.chapitre_repository = chapitre_repository

    async def exectuer(
            self, 
            chapitre_id: UUID,  
            chapitre_data: ChapitreUpdateSchema
    )-> Chapitre:
        chapitre = await self.chapitre_repository.trouver_par_id(chapitre_id)

        if not chapitre: 
            return None
        
        update_data = chapitre_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(chapitre, key, value)

        chapitre_a_jour = await self.chapitre_repository.mettre_a_jour(chapitre)
        return chapitre_a_jour