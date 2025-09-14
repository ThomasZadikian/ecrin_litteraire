from uuid import UUID
from src.domain.model.editeur import Editeur

class InMemoryEditeurRepository:
    def __init__ (self): 
        self.data: dict[UUID, Editeur] = {}

    async def sauvegarder(self, editeur: Editeur) -> None: 
        self.data[editeur.id] = editeur

    async def trouver_par_id(self, editeur_id: UUID) -> Editeur | None: 
        return self.data.get(editeur_id)
    
    async def mettre_a_jour(self, editeur: Editeur) -> Editeur | None: 
         if editeur.id in self.data:
            self.data[editeur.id] = editeur