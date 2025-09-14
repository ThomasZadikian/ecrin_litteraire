from uuid import UUID
from src.domain.model.chapitre import Chapitre
from src.domain.repository.chapitre_repository import ChapitreRepository

class RecupererUnChapitre: 
    def __init__(self, chapitre_repository: ChapitreRepository)-> None: 
        self.chapitre_repository = chapitre_repository

    async def executer(self, chapitre_id: UUID) -> Chapitre: 
        commentaire = await self.chapitre_repository.trouver_par_id(chapitre_id)
        return commentaire