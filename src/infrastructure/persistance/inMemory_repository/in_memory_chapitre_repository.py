from uuid import UUID
from src.domain.model.chapitre import Chapitre, ChapitreUpdateSchema, CreationChapitreSchema

class InMemoryChapitreRepository: 
    def __init__(self) -> None:
        self.data: dict[UUID, Chapitre] = {}

    async def sauvegarder(self, chapitre: Chapitre)-> None: 
        self.data[chapitre.id] = chapitre

    async def trouver_par_id(self, chapitre_id : UUID)-> Chapitre: 
        return self.data.get(chapitre_id)
    
    async def mettre_a_jour(
            self, 
            chapitre_data: ChapitreUpdateSchema
    ) -> Chapitre | None: 
        if chapitre_data.id in self.data: 
            self.data[chapitre_data.id] = chapitre_data